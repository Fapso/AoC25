file = open("fourth_task_test.txt")
# file = open("fourth_task_puzzle_input.txt")

storage = []

for line in file:
    line = line.rstrip("\n")
    storage_line = []
    for char in line:
        storage_line.append(char)
    storage.append(storage_line)

test_for = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

max_h = len(storage)
current = 0
x_count = 0
for level in storage:
    max_w = len(level)
    for i, o in enumerate(level):
        if o == "@":
            occupied = 0
            for pair in test_for:
                h, w = pair
                if current + h < 0:
                    continue
                if i + w < 0:
                    continue
                try:
                    other_line_h = storage[current + h]
                    picked = other_line_h[i + w]
                except IndexError:
                    continue
                if picked != ".":
                    occupied += 1
            if occupied < 4:
                storage[current][i] = "x"
                x_count += 1
    current += 1

for level in storage:
    print(level)

print(f"number of x: {x_count}")
