filepath = "data\C1_21.txt"

with open(filepath) as fp:
    lines = []
    lines = fp.readlines()
    for i in range(len(lines)):
        print(lines[len(lines) - 1 - i].rstrip())
