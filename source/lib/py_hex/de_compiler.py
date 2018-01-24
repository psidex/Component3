def de_compile(file_path):
    """
    Returns False if failed, otherwise, return script text
    """
    output = ""
    first = True

    with open(file_path, "rb") as f:
        # Skips firmware
        data = f.readlines()[15154:-2]

    for record in data:
        record = record[9:-2]  # Remove everything except data section

        if first:
            # Check for MP headers
            if record[0:4] != b"4D50":
                return False
            record = record[8:]  # Get rid of MP headers
            first = False

        last = 0
        for i in range(2, len(record), 2):
            char_num = record[last:i]
            last = i
            if char_num != b"00":  # Ignore padding
                char = chr(int(char_num.decode("utf-8"), 16))
                output += char
    
    return output

if __name__ == "__main__":
    """
    python de_compiler.py in.hex out.py
    """
    from sys import argv
    with open(argv[2], "w") as outfile:
        outfile.write(de_compile(argv[1]))
