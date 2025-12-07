from dataclasses import dataclass

# file = open("seventh_task_test.txt")
file = open("seventh_task_puzzle_input.txt")


@dataclass
class Cell:
    text: str
    pwr: int


@dataclass
class Grid:
    content: list[Cell]
    width: int
    height: int

    def get_cell(self, x, y):
        pos = y * self.width + x
        return self.content[pos]

    def get_line(self, y):
        line_start = y * self.width
        return self.content[line_start : line_start + self.width]

    # assuming there is the "S" - start somewhere
    def find_the_beggining(self):
        for i, cell in enumerate(self.content):
            if cell.text == "S":
                return (i % self.width, i // self.width)

    def read_last_line_powers(self):
        the_last_line = self.get_line(self.height - 1)
        total = 0
        for c in the_last_line:
            total += c.pwr
        return total

    def update_power(self, x, y, power):
        pos = y * self.width + x
        self.content[pos].pwr = power

    def update_text(self, x, y, text):
        pos = y * self.width + x
        self.content[pos].text = text

    def shoot_beam(self):
        for y in range(1, self.height):
            for x in range(0, self.width):
                cell = self.get_cell(x, y)
                cell_above = self.get_cell(x, y - 1)
                if cell_above.text == "|" or cell_above.text == "S":

                    if cell.text == ".":
                        self.update_text(x, y, "|")
                        self.update_power(x, y, cell_above.pwr)

                    elif cell.text == "^":
                        cell_left = self.get_cell(x - 1, y)
                        if cell_left.text == ".":
                            self.update_text(x - 1, y, "|")
                            self.update_power(x - 1, y, cell_above.pwr)
                        elif cell_left.text == "|":
                            self.update_power(x - 1, y, cell_left.pwr + cell_above.pwr)

                        cell_right = self.get_cell(x + 1, y)
                        if cell_right.text == ".":
                            self.update_text(x + 1, y, "|")
                            above_pwr = self.get_cell(x + 1, y - 1).pwr
                            self.update_power(x + 1, y, cell_above.pwr + above_pwr)

    def print_grid(self):
        the_string = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                cell = self.get_cell(x, y)
                the_string += cell.text
            the_string += "\n"
        print(the_string)


the_grid = Grid(content=[], width=0, height=0)

for y, line in enumerate(file):
    line = line.rstrip("\n")
    max_len = len(line)
    the_grid.width = max_len
    for x, char in enumerate(line):
        if char == "S":
            new_cell = Cell(text=char, pwr=1)
        else:
            new_cell = Cell(text=char, pwr=0)
        the_grid.content.append(new_cell)
    the_grid.height = y

the_grid.shoot_beam()
# the_grid.print_grid()

time_lines = the_grid.read_last_line_powers()
print(f"number of timelines: {time_lines}")
