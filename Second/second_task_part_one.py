# file = open("second_task_test.txt")
file = open("second_task_puzzle_input.txt")

the_line = file.readline()
file.close()
collection = the_line.split(",")
the_bin = []

for pair in collection:
    alpha, omega = pair.split("-")
    for i in range(int(alpha), int(omega) + 1):
        t = str(i)
        l = len(t) // 2
        a, b = t[0:l], t[(l):]
        if a == b:
            the_bin.append(t)

the_sum = 0
for n in the_bin:
    the_sum += int(n)
print(the_sum)
