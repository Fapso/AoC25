# file = open("fifth_task_test.txt")
file = open("fifth_task_puzzle_input.txt")

good_ranges = []
items = []

for line in file:
    line = line.rstrip("\n")
    if line == "":
        continue
    divider = line.find("-")
    if divider > -1:
        good_ranges.append((int(line[:divider]), int(line[divider + 1 :])))
    else:
        items.append(int(line))

fresh = []

for item in items:
    for range in good_ranges:
        first, second = range
        if first <= item <= second:
            fresh.append(item)
            break

print(f"Number of fresh items: {len(fresh)}")
