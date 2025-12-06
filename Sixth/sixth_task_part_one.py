# file = open("sixth_task_test.txt")
file = open("sixth_task_puzzle_input.txt")

total = 0
full_column = []

m = len(list(file.readline().rstrip("\n").split()))
file.seek(0)

for x in range(m):
    current_column = []
    sign = ""
    for line in file:
        line = line.rstrip("\n")
        li = list(line.split())
        n = li[x]
        try:
            nu = int(n)
            current_column.append(nu)
        except ValueError:
            sign = n
    if sign == "+":
        v = sum(current_column)
        total += v
    elif sign == "*":
        v = 1
        for z in current_column:
            v *= z
        total += v
    file.seek(0)

print(f"Total value is: {total}")
