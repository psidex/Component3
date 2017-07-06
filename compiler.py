"""
Takes a .py file, converts it into Intel HEX format, then inserts it into
the Micro:bit firmware.hex

.hex -> https://en.wikipedia.org/wiki/Intel_HEX

Heavily commented so I can actually remember how this works when I look at it
again several weeks from now

Lines commented with (?): I am not sure what they do, and have bascially just
copied from the NodeJS compiler

To run:
python3 compiler.py python_file.py
OR
without .py file argument (it will ask you for file instead)
"""
import sys

def array_to_hex_str(arr):
    """
    Given an array of integers, convert each to its hexadecimal value and
    return a string of these values
    """
    result = ""
    for item in arr:
        if item < 16:
            result += "0"  # Not sure why this happens (?)
        result += format(item, "x")  # Convert to hex
    return result

def compile(script):
    """
    An array is created called data
    This has its own headers, such as ones specific to MicroPython (I think)
    and the header also contains the file size. The array contains all the
    ASCII char codes from the script file.

    This array is then iterated over and seperated into chunks, each with their
    own headers and data. The previously created headers in "data" are also
    stored in the first chunk after its own chunk headers.

    These chunks are then converted from integers arrays to strings containing
    hexadecimal values. These are then appended to an "output" array
    """

    if len(script) > 8192:
        print("File size too large")
        sys.exit()  # Probably a better way of dealing with this

    # magic start address for inserted code
    addr = 0x3e000
    # final output array
    output = []
    # empty arary, size of header len + len of script + len of extra data in
    # each record (num of bytes, address, record type, checksum)
    data = [0] * (4 + len(script) + (16 - (4 + len(script)) % 16))
    data[0] = 77  # MicroPython headers (?)
    data[1] = 80  # ^
    data[2] = len(script) & 0xFF         # Low byte of script length
    data[3] = (len(script) >> 8) & 0xFF  # High byte
    # For each char in the script, append it's ASCII value to the array
    for i, char in enumerate(script):
        data[4 + i] = char  # script is opened as binary so this will already
                            # be the char value needed
    # Create the chunks
    for i in range(0, len(data), 16):
        chunk = [0] * 21  # New record
        chunk[0] = 16     # len of data section
        chunk[1] = (addr >> 8) & 0xff  # High byte of address
        chunk[2] = addr & 0xff         # Low byte
        chunk[3] = 0  # Data type
        checksum = 0
        for j in range(16):  # Get the next 16 chars from the data array
            chunk[4 + j] = data[i + j]
        for j in range(20):  # Create checksum
            checksum += chunk[j]
        chunk[20] = (-checksum) & 0xFF  # Low Byte of negative checksum (?)
        hexed = array_to_hex_str(chunk).upper()  # Get hex string
        print("Chunk no. {}: {}: {}".format(int(i/16), hex(addr), hexed))  # Debug
        output.append(":" + hexed)  # Add to output
        addr += 16  # Next address
    return "\n".join(output)  # Return as string with newlines inbetween chunks

"""
Takes an input file, reads it as binary, compile()s, inserts into firmware
hex, then writes to new .hex file
"""
try:
    python_file = sys.argv[1]
except IndexError:
    print("No file argument supplied")
    python_file = input("Name of file to compile: ")

print("Reading Python file")
try:
    with open(python_file, "rb") as infile:
        print("Reading firmware.txt")
        with open("firmware.txt", "r") as fw:
            data = fw.read()
            insertion_point = ":::::::::::::::::::::::::::::::::::::::::::"
            print("Compiling Python -> Intel HEX")
            compiled = compile(infile.read())
            print("Inserting into firmware")
            data = data.replace(insertion_point, compiled)

        print("Writing to new .hex file")
        with open("microbit.hex", "wb") as outfile:
            outfile.write(data.encode('utf-8'))
        print("File compiled succesfully")
except FileNotFoundError:
    print("File not found")
