import re
import sys


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    nano_robots = []
    for line in values:
        match = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line)
        if not match:
            raise Exception('unparsable line: %s' %line)

        nano_robots.append(
            (
                int(match.groups()[0]),
                int(match.groups()[1]),
                int(match.groups()[2]),
                int(match.groups()[3]),
            )
        )

    print(len(nano_robots))
    nano_robots = sorted(nano_robots, key= lambda x: x[3], reverse=True)
    max_signal_robot = nano_robots.pop(0)
    print('max signal robot: {} '.format(max_signal_robot))

    def manhattan_dist(rob1, rob2):
        return abs(rob1[0]- rob2[0]) + abs(rob1[1]- rob2[1]) + abs(rob1[2]- rob2[2])

    in_range = []
    for robot in nano_robots:
        dist = manhattan_dist(robot, max_signal_robot)
        if dist <= max_signal_robot[3]:
            in_range.append(robot)

    print('{} robots in range to {}'.format(len(in_range), max_signal_robot))


if __name__ == '__main__':
    main()
