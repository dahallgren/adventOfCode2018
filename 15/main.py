import re
import sys


class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x +other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


area = [1[2]]


def find_xy_path(start, target):
    def can_move(coord):
        if area[coord.y][coord.x] == '.':
            return coord
        else:
            return False

    (x, y) = target - start
    try:
        dx = Coord(x/abs(x), 0)
    except ZeroDivisionError:
        dx = None

    try:
        dy = Coord(0, y/abs(y))
    except ZeroDivisionError:
        dy = None

    if dy:
        y = can_move(start + dy)
    else:
        y = None

    if dx:
        x = can_move(start + dx)
    else:
        x = None

    return x, y


def find_shortest_path(area, start, target):
    path_graph = {}

    x, y = find_xy_path(start, target)

    if y:
        if y == target:
            return my_path
        else:
            my_path.append(y)
            return find_shortest_path(my_path)
    elif x:
        if x == target:
            pass
    else:
        return None


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    print(values)

if __name__ == '__main__':
    main()
