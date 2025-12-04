# file = open("fourth_task_test.txt")
file = open("fourth_task_puzzle_input.txt")

storage = []

for line in file:
    line = line.rstrip("\n")
    storage_line = []
    for char in line:
        storage_line.append(char)
    storage.append(storage_line)

test_for = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

total_x_count = 0

while True:
    max_h = len(storage)
    iter_x_count = 0
    for tier, level in enumerate(storage):
        max_w = len(level)
        for i, o in enumerate(level):
            if o == "@":
                occupied = 0
                for pair in test_for:
                    h, w = pair
                    if tier + h < 0:
                        continue
                    if i + w < 0:
                        continue
                    try:
                        other_line_h = storage[tier + h]
                        picked = other_line_h[i + w]
                    except IndexError:
                        continue
                    if picked != ".":
                        occupied += 1
                if occupied < 4:
                    storage[tier][i] = "x"
                    iter_x_count += 1
    for tier, level in enumerate(storage):
        for i, o in enumerate(level):
            if o == "x":
                storage[tier][i] = "."
    if iter_x_count == 0:
        break
    else:
        total_x_count += iter_x_count

print(f"number of x: {total_x_count}")
