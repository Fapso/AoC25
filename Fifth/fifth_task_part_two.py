# file = open("fifth_task_test.txt")
file = open("fifth_task_puzzle_input.txt")

good_ranges = []

for line in file:
    line = line.rstrip("\n")
    divider = line.find("-")
    if divider > -1:
        good_ranges.append([int(line[:divider]), int(line[divider + 1 :])])

ranges_master = list(good_ranges)
for range in good_ranges:
    f1, s1 = range
    for i, another_range in enumerate(ranges_master):
        f2, s2 = another_range
        if f1 < f2 and s1 > s2:
            ranges_master[i][0], ranges_master[i][1] = f1, s1
        elif f1 < f2 and f2 <= s1 <= s2:
            ranges_master[i][0] = f1
        elif f2 <= f1 <= s2 and s1 > s2:
            ranges_master[i][1] = s1
        elif f2 <= f1 <= s2 and f2 <= s1 <= s2:
            continue

range_set = set()
for range in ranges_master:
    range_set.add((range[0], range[1]))

the_sum = 0
for range in range_set:
    the_sum += range[1] - range[0] + 1

print(f"Number of fresh Ids: {the_sum}")
