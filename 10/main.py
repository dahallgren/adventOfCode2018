import os
import re
import sys

from time import sleep

class Point(object):
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def tick(self):
        self.x += self.vx
        self.y += self.vy

    def norm(self, xoff, yoff):
        self.x -= xoff
        self.y -= yoff

    def scale(self, xscale, yscale):
        self.x = int(float(self.x)/xscale)
        self.y = int(float(self.y)/yscale)


def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()


    points = []
    for line in values:
        match = re.match(r'position=<\s*(?P<X>[-]?\d+),\s*(?P<Y>[-]?\d+)> velocity=<\s*(?P<vx>[-]?\d+),\s*(?P<vy>[-]?\d+)>', line)
        points.append(Point(
            int(match.groupdict()['X']),
            int(match.groupdict()['Y']),
            int(match.groupdict()['vx']),
            int(match.groupdict()['vy']),
        ))

    for i in xrange(10304):
        for p in points:
            p.tick()

    min_x = min([p.x for p in points])
    max_x = max([p.x for p in points])
    min_y = min([p.y for p in points])
    max_y = max([p.y for p in points])

    os.system('clear')
    print(i, min_x, min_y, max_x, max_y)
    for p in points:
        p.norm(min_x-50, min_y-20)
        print_there(p.y, p.x, '#')
        p.tick()

    sys.stdout.flush()



if __name__ == '__main__':
    main()
