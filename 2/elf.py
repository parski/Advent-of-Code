file = open('input.txt')

class Cuboid:
    def __init__(self, length, width, height):
        self.side_a = int(length) * int(width)
        self.side_b = int(width) * int(height)
        self.side_c = int(height) * int(length)
    def smallest_side(self):
        smallest_side = self.side_a
        if smallest_side > self.side_b:
            smallest_side = self.side_b
        if smallest_side > self.side_c:
            smallest_side = self.side_c
        return smallest_side
    def area(self):
        return (self.side_a * 2) + (self.side_b * 2) + (self.side_c * 2)

def needed_area_for_cuboid(cuboid):
    split_cuboid = cuboid.split('x')
    length, width, height = split_cuboid[0], split_cuboid[1], split_cuboid[2]
    cuboid = Cuboid(length, width, height)
    return cuboid.area() + cuboid.smallest_side()

area = 0
for cuboid in file:
    area = area + needed_area_for_cuboid(cuboid)
print area
