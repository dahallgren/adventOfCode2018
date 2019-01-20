import re
import sys


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    print(values)

if __name__ == '__main__':
    main()
