# file = open("third_task_test.txt")
file = open("third_task_puzzle_input.txt")

sum_total = 0

for line in file:
    line = line.rstrip("\n")

    index_first = 0
    value_first = 0

    print(line)
    for n in range(len(line) - 1):  # we don't want to check if the last one is the biggest
        num = int(line[n])
        if num > value_first:
            value_first = num
            index_first = n
    print(index_first, value_first)
    line_cut = line[index_first + 1 :]
    print(line_cut)

    index_second = 0
    value_second = 0

    for i, n in enumerate(line_cut):
        num = int(n)
        if num > value_second:
            value_second = num
            index_second = i
    print(index_second, value_second)
    con = line[index_first] + line_cut[index_second]

    sum_total += int(con)

print(f"Total sum is: {sum_total}")
