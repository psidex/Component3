def de_compile(file_path):
    """
    Returns -1 if failed, otherwise, return script text
    """
    output = ""
    first = True

    with open(file_path, "rb") as f:
        # Skips firmware.hex
        data = f.readlines()[15155:-2]

    for record in data:
        if first:
            # Check for MP headers then ignore MP headers
            if record[9:13] != b"4D50":
                return -1
            data = record[17:-2]
            first = False
        else:
            data = record[9:-2]
        chunk = []
        last = 0
        for x in range(2, len(data), 2):
            chunk.append(data[last:x])
            last = x
        for y in chunk:
            c = chr(int(y.decode("utf-8"), 16))
            if c != None:
                output += c
    return output

if __name__ == "__main__":
    print(de_compile("microbit.hex"))
