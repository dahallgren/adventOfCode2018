"""
Day 6
"""
import re
import sys

from collections import Counter


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    values = [(int(x), int(y)) for x, y in [value.split(',') for value in values]]

    coordinates = {}
    for i, coord in enumerate(values):
        coordinates['c{}'.format(i)] = coord


    min_x = min(values)[0]
    max_x = max(values)[0]
    min_y = min(values, key=lambda coord:coord[1])[1]
    max_y = max(values, key=lambda coord: coord[1])[1]

    print('boundaries: x: {} to {}, y: {} to {}'.format(min_x, max_x, min_y, max_y))

    def manhattan_distance(coord_A, coord_B):
        return abs(coord_A[0] - coord_B[0]) + abs(coord_A[1]-coord_B[1])

    nearest_coords = []
    reg_size = 0
    boundary_coords = set()
    for y in range(min_y, max_y +1):
        for x in range(min_x, max_x +1):
            min_dist = None
            nearest = None
            dists = []
            for coord_key, coord_value in coordinates.iteritems():
                dist = manhattan_distance((x, y), coord_value)
                dists.append(dist)
                if min_dist is None or dist < min_dist:
                    min_dist = dist
                    nearest = coord_key

            if sum(dists) < 10000:
                reg_size += 1

            if x in (min_x, max_x):
                boundary_coords.add(nearest)

            if y in (min_y, max_y):
                boundary_coords.add(nearest)

            if Counter(dists)[min_dist] > 1:
                nearest = 'multiple'

            if nearest != 'multiple':
                nearest_coords.append(nearest)
            # print('({}, {}) -> {}'.format(x, y, nearest))

    areas = Counter(nearest_coords)

    # print('boundary coordinates: {}'.format(boundary_coords))
    max_area = None
    for i in sorted(zip(areas.values(), areas.keys()), reverse=True)[:5]:
        print(i, coordinates[i[1]])
        if not max_area and i[1] not in boundary_coords:
            max_area = i

    print("Part one: choose {}".format(max_area))
    print("size of largest area with total distance < 10000: {}".format(reg_size))


if __name__ == '__main__':
    main()
