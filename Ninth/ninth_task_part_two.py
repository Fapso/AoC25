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
borders = set()


def get_position(x, y):
    pos = y * max_x + x
    return positions[pos]


def calculate_fields(x1, y1, x2, y2):
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    return w * h


def calculate_distance(x1, y1, x2, y2):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return [w, h]


def row_of_borders(y):
    lizz = []
    for b in borders:
        if b[1] == y:
            lizz.append(b)
    return lizz


def column_of_borders(x):
    lizz = []
    for b in borders:
        if b[0] == x:
            lizz.append(b)
    return lizz


def check_if_there_is_border_in_all_direction(x, y, rows, columns):
    found_left = False
    found_right = False
    found_up = False
    found_down = False

    for pair in rows:
        xp, _ = map(int, pair)
        if pair in borders:
            if xp < x:
                found_left = True
            elif xp > x:
                found_right = True
            if found_left and found_right:
                break

    for pair in columns:
        _, yp = map(int, pair)
        if pair in borders:
            if yp < y:
                found_up = True
            elif yp > y:
                found_down = True
            if found_up and found_down:
                break

    if found_left and found_right and found_up and found_down:
        return True
    return False


def can_be_drawn(i, j):
    xi, yi = map(int, positions[i])
    xj, yj = map(int, positions[j])

    w = abs(xj - xi) + 1
    h = abs(yj - yi) + 1

    for o in range(w):
        cell = xi + o, yi
        if cell in borders:
            continue
        columns = column_of_borders(cell[0])
        rows = row_of_borders(cell[1])
        is_it = check_if_there_is_border_in_all_direction(cell[0], cell[1], rows, columns)
        if not is_it:
            return False
    for o in range(w):
        cell = xj - o, yj
        if cell in borders:
            continue
        columns = column_of_borders(cell[0])
        rows = row_of_borders(cell[1])
        is_it = check_if_there_is_border_in_all_direction(cell[0], cell[1], rows, columns)
        if not is_it:
            return False
    for o in range(h):
        cell = xi, yi + o
        if cell in borders:
            continue
        columns = column_of_borders(cell[0])
        rows = row_of_borders(cell[1])
        is_it = check_if_there_is_border_in_all_direction(cell[0], cell[1], rows, columns)
        if not is_it:
            return False
    for o in range(h):
        cell = xj, yj - o
        if cell in borders:
            continue
        columns = column_of_borders(cell[0])
        rows = row_of_borders(cell[1])
        is_it = check_if_there_is_border_in_all_direction(cell[0], cell[1], rows, columns)
        if not is_it:
            return False

    return True


biggest_pair = []
biggest_field = 0

already_checked = set()


for i, p in enumerate(positions):
    x1, y1 = map(int, p)

    distances = []

    for j, q in enumerate(positions):
        if i == j:
            continue
        if j in already_checked:
            continue

        x2, y2 = map(int, q)
        x0, y0 = calculate_distance(x1, y1, x2, y2)
        if x0 == 0:
            distances.append([i, x0, y0])
        if y0 == 0:
            distances.append([i, x0, y0])

    already_checked.add(i)

    if distances:
        for r, x, y in distances:  # this can be remade faster
            cell = positions[r]
            if x == 0:
                for v in range(y + 1):
                    borders.add((cell[0], cell[1] + v))
            if y == 0:
                for v in range(x + 1):
                    borders.add((cell[0] + v, cell[1]))


sorted_list = list(borders)
sorted_list.sort(key=lambda t: (t[1], t[0]))

allowed_field = set()

for i, p in enumerate(positions):

    distances = []

    for j, q in enumerate(positions):
        if i == j:
            continue
        can = can_be_drawn(i, j)
        if can:
            x1, y1 = map(int, p)
            x2, y2 = map(int, q)
            fields = calculate_fields(x1, y1, x2, y2)

            if fields > biggest_field:
                biggest_field = fields
                biggest_pair = [p, q]

    already_checked.add(i)

# aaaa = list(borders)
# aaaa.sort(key=lambda t: (t[1], t[0]))

print(f"The biggest possible carpet: {biggest_field}")
print(f"The pair of opposite starting points: {biggest_pair}")
