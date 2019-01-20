import sys


def find_differ_by_one(line1, line2):
    match = 0
    idx = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            idx = i
            match += 1

    return (match == 1, idx)

def main(args):
    with open(args, 'r') as s:
        values = s.readlines()

    while values:
        line = values.pop(0).rstrip('\n')
        for line2 in values:
            match, idx = find_differ_by_one(line, line2)
            if match:
                print('line {} and line {} differ by one at {}'.format(
                    line,
                    line2,
                    idx
                ))
                result = list(line)
                result.pop(idx)
                print('result {}'.format(''.join(result)))
                break


if __name__ == '__main__':
    main(sys.argv[1])
