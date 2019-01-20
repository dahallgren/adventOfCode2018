import re
import sys

def calc_power_level(x, y, serial):
    rack_id = x +10
    power_level = (rack_id*y) + serial
    power_level = power_level * rack_id
    try:
        hundred_digit = int(str(power_level)[-3])
    except IndexError:
        hundred_digit = 0

    return hundred_digit - 5


def main():
    serial = int(sys.argv[1])

    grid = [[ '#' for y in range(300)] for x in range(300)]

    for y in range(1, 301):
        for x in range(1, 301):
            grid[x-1][y-1] = calc_power_level(x, y, serial)

    total_power = {}
    for size in range(1, 299):
        print(size)
        for y in range(300-size):
            for x in range(300-size):
                power = 0
                for ix in range(size):
                    for iy in range(size):
                        power += grid[x+ix][y+iy]
                total_power[(x+1, y+1, size)] = power

    print(max(zip(total_power.values(), total_power.keys())))


if __name__ == '__main__':
    main()
