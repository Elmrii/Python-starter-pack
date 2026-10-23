def sum_num_file(path):
    file = open(path, "r")
    total = 0
    for line in file:
        if line.strip() != "":
            total += float(line.strip())
    file.close()
    return round(total, 3)
filename = "expenses.txt"
print("Total expenses:", sum_num_file(filename))
