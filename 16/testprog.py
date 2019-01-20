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

    register[0] = 0
    register[1] = 0
    register[2] = 0
    register[3] = 0

    for line in values:
        match = re.match(r'^(\d+) (\d) (\d) (\d)$', line)
        if not match:
            raise

        op = op_codes[int(match.groups()[0])]
        oper = instructions[op]

        # run op
        oper(int(match.groups()[1]), int(match.groups()[2]), int(match.groups()[3]))

    print(register)

if __name__ == '__main__':
    main()
