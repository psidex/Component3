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
        last = 0        
        record = record[9:-2]  # Remove everything except data section
        for c in range(2, len(record), 2):
            char = record[last:c]
            last = c
            c = chr(int(char.decode("utf-8"), 16))
            if c != None:
                output += c
    
    if output[0:2] != "MP":
        return False
    return output[2:]

if __name__ == "__main__":
    """
    python de_compiler.py in.hex out.py
    """
    from sys import argv
    with open(argv[2], "w") as outfile:
        outfile.write(de_compile(argv[1]))
