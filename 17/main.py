import copy
import re
import sys


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    clays = set()

    for line in values:
        xmatch = re.match(r'.*x=(\d+)\.?\.?(\d*)', line)
        ymatch = re.match(r'.*y=(\d+)\.?\.?(\d*)', line)

        if not xmatch:
            raise
        if not ymatch:
            raise

        if xmatch.groups()[1]:
            for x in range(int(xmatch.groups()[0]), int(xmatch.groups()[1]) + 1):
                clays.add((int(ymatch.groups()[0]), x),)

        if ymatch.groups()[1]:
            for y in range(int(ymatch.groups()[0]), int(ymatch.groups()[1]) + 1):
                clays.add((y, int(xmatch.groups()[0])), )

    min_x = min(clays, key=lambda coord: coord[1])[1]
    max_x = max(clays, key=lambda coord: coord[1])[1]
    min_y = min(clays, key=lambda coord: coord[0])[0]
    max_y = max(clays, key=lambda coord: coord[0])[0]

    print("min_x {}".format(min_x))
    print("max_x {}".format(max_x))
    print("min_y {}".format(min_y))
    print("max_y {}".format(max_y))
    print(len(clays))

    # add origin of water flow
    source = set([(0, 500),])

    stops = set(sorted(copy.copy(clays)))

    bottom_reached = False

    fills = set()
    running_water = set()

    while source:
        drip = source.pop()
        # print('popping water flow at {}'.format(drip))

        # find clay
        y = drip[0]
        x = drip[1]
        while (y + 1, x) not in stops:
            y += 1
            if y < min_y:
                continue
            running_water.add((y, x),)
            if y >= max_y:
                bottom_reached = True
                break

        if bottom_reached:
            bottom_reached = False
            continue

        # Clay found
        open_left = False
        open_right = False

        # go left
        xl = x
        while (y, xl - 1) not in stops:
            xl -= 1
            if (y + 1, xl -1) not in stops:
                # open left found
                xl -= 1
                open_left = True
                break

        # go right
        xr = x
        while (y, xr + 1) not in stops:
            xr += 1
            if (y + 1, xr + 1) not in stops:
                # open right found
                xr += 1
                open_right = True
                break

        if not open_left and not open_right:
            # fill
            # print("filling at {}, {}..{}".format(y, xl, xr))
            for fill_x in range(xl, xr + 1):
                fills.add((y, fill_x),)
                stops.add((y, fill_x),)

            if xl == xr:
                # print('fill just vertical')
                fills.add((y, xl),)
                stops.add((y, xl),)
            if drip[0] < y:
                source.add(drip)
            else:
                # special case, add original source
                source.add((0, 500))
        else:
            for run_water in range(xl, xr + 1):
                running_water.add((y, run_water), )

        if open_left:
            source.add((y, xl),)

        if open_right:
            source.add((y, xr),)

    for y in range(0, max_y + 1):
        sys.stdout.write('{:<4}'.format(y))
        for x in range(min_x, max_x + 5):
            if (y, x) in fills:
                sys.stdout.write('~')
            elif (y, x) in running_water:
                sys.stdout.write('|')
            elif (y, x) in clays:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print('')

    print(len(fills.union(running_water)))
    print(len(fills))


if __name__ == '__main__':
    main()
