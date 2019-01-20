import re
import sys


def main(args):
    with open(args, 'r') as s:
        values = s.readlines()

    fabric = [['.' for x in range(1000)] for y in range(1000)]
    overlap = 0
    claims_not_overlapping = set()

    for value in values:
        claim = re.match(r'#(?P<id>\d+) @ (?P<left_start>\d+),(?P<top_start>\d+): (?P<width>\d+)x(?P<height>\d+)',
                         value)\
            .groupdict()

        xstart = int(claim['left_start'])
        xend = xstart + int(claim['width'])
        ystart = int(claim['top_start'])
        yend = ystart + int(claim['height'])

        claims_not_overlapping.add(claim['id'])
        for y in range(ystart, yend):

            for x in range(xstart, xend):
                try:
                    if fabric[y][x] == '.':
                        #empty slot
                        fabric[y][x] = '#{}'.format(claim['id'])
                    elif fabric[y][x].startswith('#'):
                        overlap += 1
                        fabric[y][x] = '{}#{}'.format(fabric[y][x], claim['id'])
                        ids = fabric[y][x][1:].split('#')
                        for id in ids:
                            if id in claims_not_overlapping:
                                claims_not_overlapping.remove(id)

                    if fabric[y][x].count('#') > 2:
                        # Already counted
                        overlap -= 1

                except IndexError:
                    print(claim)
                    raise
                except KeyError:
                    print(ids)
                    print(fabric[y][x])
                    print(claims_not_overlapping)
                    raise

    print('claim {} does not overlap'.format(claims_not_overlapping))

#    for y in range(1000):
#        for x in range(1000):
#            sys.stdout.write(fabric[y][x])
#        print('')

    print('overlap {}'.format(overlap))

if __name__ == '__main__':
    main(sys.argv[1])
