"""
TO FIX
Compiling is missing the last bracket and \n in this script:
```
from microbit import *

while True:
    display.scroll("1234")
    sleep(500)

```
Mightbe because the script needs to be padded
with 0's before it is iterated over to produce
the .hex
"""

def compile_to_hex(script_bin):
    script_size = len(script_bin)
    if script_size > 0x2000:
        return False

    addr = 0x3e000  # Magic start address for inserted code
    output = []     # Final output
    offset = 0      # Location in script

    # Prepend header + low + high bytes of script length
    script_bin = b"\x4D\x50" + bytes([script_size & 0xFF]) + bytes([(script_size >> 8) & 0xFF]) + script_bin

    for i in range(0, script_size, 16):
        record = []
        record.append(0x10)                # Len of data section
        record.append((addr >> 8) & 0xff)  # High byte of address
        record.append(addr & 0xff)         # Low byte
        record.append(0x0)                 # Data type
        for i in range(16):                # 16 chars from script
            try:
                record.append(script_bin[offset + i])
            except IndexError:
                record.append(0x00)  # Script finished, pad with 0s
        # Checksum - twos complement of record+, then get low byte
        record.append(((sum(record) ^ 0xFF) + 0x1) & 0xFF)
        output.append(":" + "".join("{:02x}".format(x) for x in record).upper())
        addr += 16    # Next address
        offset += 16  # Next script location

    with open("res/micropython/micropython.hex", "r") as fw:
        data = fw.read()
    insertion_point = ":::::::::::::::::::::::::::::::::::::::::::"
    data = data.replace(insertion_point, "\n".join(output))
    return data.encode("utf-8")

if __name__ == "__main__":
    """
    python compiler.py in.py out.hex
    """
    from sys import argv
    python_file = argv[1]
    out_file = argv[2]
    with open(python_file, "rb") as f_in:
        s = f_in.read()
    with open(out_file, "wb") as outfile:
        outfile.write(compile_to_hex(s))
