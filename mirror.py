def mirror(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    file = open(path, "w")
    for line in lines:
        if line.endswith("\n"):
            file.write(line[:-1][::-1] + "\n")
        else: file.write(line[::-1])
    file.close()
