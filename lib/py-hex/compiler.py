def compile_to_hex(script, script_size):
    """
    Creates an array that contains the necessary things to be compiled, then, 16
    at a time, pull values from that array and convert them to Intel HEX format,
    when finished, insert the script into firmware.hex and return it as encoded
    data. Returns -1 if failed
    """
    if script_size > 0x2000:
        return -1

    addr = 0x3e000  # Magic start address for inserted code
    output = []  # Final output
    data = [0] * 4
    data[0] = 77  # "MicroPython signature"
    data[1] = 80  # ^
    data[2] = script_size & 0xFF         # Low byte of script length
    data[3] = (script_size >> 8) & 0xFF  # High byte

    for i, char_val in enumerate(script):
        data.append(char_val)  # Append every char value to data array

    # Pad out array with 0's so the last chunk will have the correct length
    data = data + [b for b in bytes(16 - len(data) % 16)]

    # Create chunks
    for i in range(0, len(data), 16):
        chunk = []        # New record
        chunk.append(16)  # len of data section in bytes
        chunk.append((addr >> 8) & 0xff)  # High byte of address
        chunk.append(addr & 0xff)         # Low byte
        chunk.append(0)      # Data type
        for j in range(16):  # Get the next 16 chars from the data array
            chunk.append(data[i + j])
        # Checksum - The low byte of the negative of the sum of the chunk
        chunk.append((-sum(chunk)) & 0xFF)
        # ":" + (Array of ints -> string of hex values)
        output.append(":" + "".join("{:02x}".format(x) for x in chunk).upper())
        addr += 16  # Next address

    with open("micropython.hex", "r") as fw:
        data = fw.read()
    insertion_point = ":::::::::::::::::::::::::::::::::::::::::::"
    data = data.replace(insertion_point, "\n".join(output))
    return data.encode("utf-8")

if __name__ == "__main__":
    """
    python compiler.py in.py out.hex
    """
    from os import fstat
    from sys import argv
    python_file = argv[1]
    out_file = argv[2]
    with open(python_file, "rb") as f_in:
        s = f_in.read()
        s_size = fstat(f_in.fileno()).st_size  # File size size from fstat
    with open(out_file, "wb") as outfile:
        outfile.write(compile_to_hex(s, s_size))
