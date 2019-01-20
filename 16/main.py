"""
Day 16, opcodes
"""

import re
import sys


# registers
register = [0, 0, 0, 0]

# opcodes
def _addr(ra, rb, rc):
    register[rc] = register[ra] + register[rb]

def _addi(ra, val_b, rc):
    register[rc] = register[ra] + val_b

def _mulr(ra, rb, rc):
    register[rc] = register[ra] * register[rb]

def _muli(ra, val_b, rc):
    register[rc] = register[ra] * val_b

def _banr(ra, rb, rc):
    register[rc] = register[ra] & register[rb]

def _bani(ra, val_b, rc):
    register[rc] = register[ra] & val_b

def _borr(ra, rb, rc):
    register[rc] = register[ra] | register[rb]

def _bori(ra, val_b, rc):
    register[rc] = register[ra] | val_b

def _setr(ra, rb, rc):
    register[rc] = register[ra]

def _seti(val_a, val_b, rc):
    register[rc] = val_a

def _gtir(val_a, rb, rc):
    if val_a > register[rb]:
        register[rc] = 1
    else:
        register[rc] = 0

def _gtri(ra, val_b, rc):
    if register[ra] > val_b:
        register[rc] = 1
    else:
        register[rc] = 0

def _gtrr(ra, rb, rc):
    if register[ra] > register[rb]:
        register[rc] = 1
    else:
        register[rc] = 0

def _eqir(val_a, rb, rc):
    if val_a == register[rb]:
        register[rc] = 1
    else:
        register[rc] = 0

def _eqri(ra, val_b, rc):
    if register[ra] == val_b:
        register[rc] = 1
    else:
        register[rc] = 0

def _eqrr(ra, rb, rc):
    if register[ra] == register[rb]:
        register[rc] = 1
    else:
        register[rc] = 0


instructions = {
    'addr': _addr,
    'addi': _addi,
    'mulr': _mulr,
    'muli': _muli,
    'banr': _banr,
    'bani': _bani,
    'borr': _borr,
    'bori': _bori,
    'setr': _setr,
    'seti': _seti,
    'gtir': _gtir,
    'gtri': _gtri,
    'gtrr': _gtrr,
    'eqir': _eqir,
    'eqri': _eqri,
    'eqrr': _eqrr
}


op_codes = {
    0:  'muli',
    1:  'borr',
    2:  'gtri',
    3:  'eqri',
    4:  'gtrr',
    5:  'eqir',
    6:  'addi',
    7:  'setr',
    8:  'mulr',
    9:  'addr',
    10: 'bori',
    11: 'bani',
    12: 'seti',
    13: 'eqrr',
    14: 'banr',
    15: 'gtir',
}


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()

    samples = []

    for line in values:
        match = re.match(r'Before: \[(\d), (\d), (\d), (\d)\]$', line)
        if match:
            before = [int(match.groups()[0]), int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3])]

        match = re.match(r'^(\d+) (\d) (\d) (\d)$', line)
        if match:
            instr = [int(match.groups()[0]), int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3])]

        match = re.match(r'After:  \[(\d), (\d), (\d), (\d)\]$', line)
        if match:
            after = [int(match.groups()[0]), int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3])]
            samples.append(dict(
                instr=instr,
                before=before,
                after=after
            ))

    matching = {}
    not_matching = {}
    three_or_more = 0
    for sample in samples:
        matched = 0
        for op, oper in instructions.iteritems():

            # set inital value:
            for idx in range(4):
                register[idx] = sample['before'][idx]

            # run op
            oper(sample['instr'][1], sample['instr'][2], sample['instr'][3])
            # compare output
            if register[0] == sample['after'][0] and\
               register[1] == sample['after'][1] and\
               register[2] == sample['after'][2] and\
               register[3] == sample['after'][3]:
                # print('instr {} behaves like op {}'.format(sample['instr'][0], op))
                matching.setdefault(sample['instr'][0], set()).add(op)
                matched += 1
            else:
                not_matching.setdefault(sample['instr'][0], set()).add(op)

        if not matched:
            raise Exception("sample {} didn't match anything".format(sample))

        if matched >= 3:
            three_or_more += 1

    print('Part1: {} samples matched 3 or more instructions'.format(three_or_more))
    print('')
    op_codes_candidates = {}
    for instr in range(16):
        op_codes_candidates[instr] = matching[instr] - not_matching[instr]
        print('{:<2}: {}'.format(instr, list(op_codes_candidates[instr])))
    print('Above could be manually reduced to one unique name per code which gives:')
    print('')
    for op, name in op_codes.iteritems():
        print('{:<2}: {}'.format(op, name))


if __name__ == '__main__':
    main()
