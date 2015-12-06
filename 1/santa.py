file = open('input.txt')
floor = 0
for line in file:
    for character in line:
        if character == '(':
            floor = floor + 1
        elif character == ')':
            floor = floor - 1
print floor
