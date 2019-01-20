import re
import sys


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    letters = [hex(i)[2:].decode('hex') for i in range(97, 123)]

    res = {}

    # Part 1, uncomment this
    # letters = ['']

    for letter in letters:

        line = re.sub(r'{}|{}'.format(letter, letter.upper()), "", values[0])

        print('start length : {}'.format(len(line)))
        substring = list(line.rstrip('\n'))

        idx = 0
        last_idx = len(substring) - 2
        while idx <= last_idx:
            if substring[idx].isupper():
                if substring[idx+1] == substring[idx].lower():
                    substring.pop(idx)
                    substring.pop(idx)
                    last_idx -= 2
                    idx -= 2
            else:
                if substring[idx+1] == substring[idx].upper():
                    substring.pop(idx)
                    substring.pop(idx)
                    last_idx -= 2
                    idx -= 2

            idx = max(0, idx + 1)

        print('{}: remaining length {}'.format(letter.upper(), len(''.join(substring))))
        res[letter] = len(''.join(substring))

    length, letter = min(zip(res.values(), res.keys()))
    print('min length: {} for unit {}/{}'.format(length, letter, letter.upper()))


if __name__ == '__main__':
    main()
