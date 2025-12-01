# file = open("first_task_test.txt")
file = open("first_task_puzzle_input.txt")

position = 50
zeroes = 0

for line in file:
    line = line.rstrip("\n")
    left_or_right = line[0]
    movement = line[1:]
    movement = int(movement)
    if left_or_right == "L":
        position -= movement
    elif left_or_right == "R":
        position += movement
    if position % 100 == 0:
        zeroes += 1

print(f"amount of zeroes: {zeroes}")
