# file = open("sixth_task_test.txt")
file = open("sixth_task_puzzle_input.txt")

total = 0

operator_positions = []

for line in file:
    for i, char in enumerate(line):
        if char == "+" or char == "*":
            operator_positions.append(i)

for i, operator_pos in enumerate(operator_positions):
    file.seek(0)
    string_collection = []
    operator = ""
    for line in file:
        line = line.rstrip("\n")
        if i < len(operator_positions) - 1:
            text = line[operator_pos : operator_positions[i + 1] - 1]
        else:
            text = line[operator_pos:]
        try:
            int(text)
            string_collection.append(text)
        except ValueError:
            if "+" in text:
                operator = "+"
            elif "*" in text:
                operator = "*"
    previous = operator_pos

    strings_reversed = []
    for word in string_collection:
        strings_reversed.append(word[::-1])

    actual_values = []
    max_index = len(strings_reversed[0])
    for x in range(max_index):
        new_word = ""
        for word in strings_reversed:
            new_word += word[x]
        number = int(new_word)
        actual_values.append(number)

    if operator == "+":
        total += sum(actual_values)
    elif operator == "*":
        v = 1
        for a in actual_values:
            v *= a
        total += v

print(f"Total value is: {total}")
