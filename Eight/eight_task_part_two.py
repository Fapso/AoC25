import math

# file = open("eight_task_test.txt")
file = open("eight_task_puzzle_input.txt")


def calculate_distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return d


positions = []

for line in file:
    line = line.rstrip("\n")
    line = line.split(",")
    positions.append(line)


def merry_go_around():
    distances_shortest = []

    already_checked = set()

    for i, p in enumerate(positions):
        x1, y1, z1 = map(int, p)

        distances = []

        for x, q in enumerate(positions):
            if i == x:
                continue
            if x in already_checked:
                continue

            x2, y2, z2 = map(int, q)
            distance = calculate_distance(x1, y1, z1, x2, y2, z2)

            distances.append([i, x, distance])

        already_checked.add(i)

        if not distances:
            continue

        for dist in distances:
            distances_shortest.append(dist)

    distances_shortest.sort(key=lambda t: t[2])
    picked_connections = distances_shortest

    all_positions = set()
    for x, y, _ in distances_shortest:
        all_positions.add(x)
        all_positions.add(y)

    circuits = []
    for p in all_positions:
        circuits.append(set([p]))

    while len(circuits) > 1:
        for pair in picked_connections:
            x1, y1, _ = pair

            if any([x1 in s and y1 in s for s in circuits]):
                continue

            set_with_x1 = None
            for i, s in enumerate(circuits):
                if x1 in s:
                    set_with_x1 = s
                    del circuits[i]

            set_with_y1 = None
            for i, s in enumerate(circuits):
                if y1 in s:
                    set_with_y1 = s
                    del circuits[i]

            combined_set = set_with_x1 | set_with_y1
            circuits.append(combined_set)

            if len(circuits) == 1:
                one = int(positions[x1][0])
                two = int(positions[y1][0])
                print(one * two)

    circuits_list = [len(x) for x in circuits]
    circuits_list.sort(key=lambda t: t, reverse=True)
    cut = circuits_list[0:3]
    a = 1
    for cu in cut:
        a *= cu


merry_go_around()
