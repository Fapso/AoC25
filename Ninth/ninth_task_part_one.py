# file = open("ninth_task_test.txt")
file = open("ninth_task_puzzle_input.txt")


positions = []  # x, y

max_y = 0
max_x = 0

for line in file:
    line = line.rstrip("\n")
    x, y = line.split(",")
    x, y = int(x), int(y)
    positions.append([x, y])  # x, y
    if y > max_y:
        max_y = y
    if x > max_x:
        max_x = x

positions.sort(key=lambda t: (t[1], t[0]))


def calculate_fields(x1, y1, x2, y2):
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    return w * h


biggest_pair = []
biggest_field = 0

already_checked = set()

for i, p in enumerate(positions):
    x1, y1 = map(int, p)

    for j, q in enumerate(positions):
        if i == j:
            continue
        if j in already_checked:
            continue

        x2, y2 = map(int, q)
        fields = calculate_fields(x1, y1, x2, y2)

        if fields > biggest_field:
            biggest_field = fields
            biggest_pair = [p, q]

    already_checked.add(i)


print(f"The biggest possible carpet: {biggest_field}")
print(f"The pair of opposite starting points: {biggest_pair}")
