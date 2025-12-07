# file = open("seventh_task_test.txt")
file = open("seventh_task_puzzle_input.txt")

sum_beams = 0
splits = 0

possible_beam_positions = []

for line in file:
    line = line.rstrip("\n")
    max_len = len(line)

    next_line_possible_beam_positions = []
    a = ""
    for i, char in enumerate(line):
        if i in possible_beam_positions:
            if char == "|" or char == ".":
                next_line_possible_beam_positions.append(i)
                char = "|"
                a += char
            elif char == "^":
                if i - 1 > -1:
                    next_line_possible_beam_positions.append(i - 1)
                if i + 1 <= max_len:
                    next_line_possible_beam_positions.append(i + 1)
                char = "^"
                a += char
                splits += 1
            continue
        if char == "S":
            a += char
            next_line_possible_beam_positions.append(i)
        if char == ".":
            a += char
        if char == "^":
            a += char
    sum_beams += a.count("|")

    possible_beam_positions = list(next_line_possible_beam_positions)

print(f"Number of beams: {sum_beams}")
print(f"Number of splits: {splits}")
