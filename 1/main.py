import sys


def main(args):
    total = 0
    freqs_ones = set([0])
    freqs_twice = set()
    with open(args, 'r') as s:
        values = s.readlines()

    modulus = len(values)
    idx = 0
    print('modulus {}'.format(modulus))
    iters = 0
    while True:
        x = values[idx]
        total += int(x.lstrip('+'))
        if total in freqs_ones:
            print('freq. {} reached twice after {} iterations'.format(total, iters))
            break
        else:
            freqs_ones.add(total)
        idx = (idx + 1)%modulus
        iters += 1


if __name__ == '__main__':
    main(sys.argv[1])
