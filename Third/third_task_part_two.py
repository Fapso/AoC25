# file = open("third_task_test.txt")
file = open("third_task_puzzle_input.txt")

batteries = 12
sum_total = 0

for line in file:
    line = line.rstrip("\n")

    index_cut = 0

    stuff = ""
    for i in range(batteries):
        biggest = 0
        add_to_index = 0
        batteries_left = batteries - i - 1

        line_cut = line[index_cut + i : len(line) - batteries_left]

        for x, y in enumerate(line_cut):
            num = int(y)

            if num > biggest:
                add_to_index = x
                biggest = num

        index_cut += add_to_index
        stuff += str(biggest)

    add_this = int(stuff)
    sum_total += add_this

print(f"Total sum is: {sum_total}")
