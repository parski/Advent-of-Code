file = open('input.txt')

grid = [[False] * 1000 for x in range(1000)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.__bottom_left = bottom_left
        self.__top_right = top_right
    def column_range(self):
        return range(int(self.__bottom_left().x), int(self.__top_right().x) + 1)
    def row_range(self):
        return range(int(self.__bottom_left().y), int(self.__top_right().y) + 1)

class Instruction:
    def __init__(self, instruction):
        self.components = instruction.split()
    def operation(self):
        # shitlang got no enum fam
        if self.components[0] == 'toggle':
            return 'toggle'
        elif self.components[1] == 'on':
            return 'on'
        else:
            return 'off'
    def __point_from_component(self, component):
        (x, y) = component.split(',')
        return Point(x, y)
    def __first_point(self):
        first_point_component = self.components[len(self.components) - 3]
        return self.__point_from_component(first_point_component)
    def __second_point(self):
        second_point_component = self.components[len(self.components) - 1]
        return self.__point_from_component(second_point_component)
    def rectangle(self):
        return Rectangle(self.__first_point, self.__second_point)

def turn_on(rectangle):
    for column in rectangle.column_range():
        for row in rectangle.row_range():
            grid[column][row] = True 

def turn_off(rectangle):
    for column in rectangle.column_range():
        for row in rectangle.row_range():
            grid[column][row] = False

def toggle(rectangle):
    for column in rectangle.column_range():
        for row in rectangle.row_range():
            grid[column][row] = not grid[column][row]

def parse_instruction(instruction):
    operation = instruction.operation()
    rectangle = instruction.rectangle()
    if operation == 'toggle':
        toggle(rectangle)
    elif operation == 'on':
        turn_on(rectangle)
    else:
        turn_off(rectangle)

for line in file:
    parse_instruction(Instruction(line))

light_count = 0
for column in grid:
    for row in column:
        if row == True:
            light_count += 1

print(light_count)

