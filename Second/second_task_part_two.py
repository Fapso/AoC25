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
        allowed_l = []

        for x in range(len(t) - 1):
            if len(t) % (x + 1) == 0:
                allowed_l.append(x + 1)
        for l in allowed_l:
            dumpy = [t[y : y + l] for y in range(0, len(t), l)]
            co = set()
            for z in dumpy:
                co.add(z)
            if len(co) == 1:
                the_bin.append(t)
                break

the_sum = 0
for n in the_bin:
    the_sum += int(n)

print(f"the sum : {the_sum}")
