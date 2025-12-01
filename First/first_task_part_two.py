# file = open("first_task_test.txt")
file = open("first_task_puzzle_input.txt")

position = 50
zeroes = 0
crossed = 0


for line in file:
    line = line.rstrip("\n")
    left_or_right = line[0]
    movement = line[1:]
    movement = int(movement)
    original_position = int(position)
    sign = ""
    add_crossed = 0

    full_rotations = abs(movement // 100)
    add_crossed += full_rotations
    movement = movement % 100
    if left_or_right == "L":
        if movement > position:
            position = position + 100 - movement
            if original_position != 0:
                add_crossed += 1
        else:
            position -= movement
    elif left_or_right == "R":
        if movement > (100 - position):
            position = position - (100 - movement)
            if original_position != 0:
                add_crossed += 1
        else:
            position += movement
    if position % 100 == 0:
        zeroes += 1
    position %= 100
    crossed += add_crossed


print(f"zeroes: {zeroes}")
print(f"crossed: {crossed}")
print(f"zeroes and crossed: {zeroes + crossed}")
