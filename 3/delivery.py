file = open('input.txt')

x, y = 0, 0
houses = set([(x, y)])

for character in file.read():
    if character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    elif character == '>':
        x += 1
    elif character == '<':
        x -= 1
    houses.add((x, y))

print(len(houses))

