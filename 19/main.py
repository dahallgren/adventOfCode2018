"""
Day 19, opcodes with flow control
"""

import re
import sys


# 6 registers, 0 to 5
register = [0, 0, 0, 0, 0, 0]
ip_reg = 0

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
            start_ip = s.readline()
            values = s.readlines()

    match = re.match(r'^#ip (\d)$', start_ip)
    ip_reg = int(match.groups()[0])
    print('ip in register %s' % ip_reg)

    mem = []

    for line in values:
        match = re.match(r'^(\w+) (\d+) (\d+) (\d+)$', line)

        mem.append((
            match.groups()[0],
            int(match.groups()[1]),
            int(match.groups()[2]),
            int(match.groups()[3])
        ))

    print('run program')

    count = 0
    ip = 0
    while True:
        try:
            register[ip_reg] = ip
            instr = mem[ip]
            op = instructions[instr[0]]
            print(instr[0], instr[1], instr[2], instr[3])
            op(instr[1], instr[2], instr[3])
            print(register)
            ip = register[ip_reg]
            ip += 1
            count += 1
            # raw_input()
        except IndexError:
            print('Segmentation fault at %s' %( ip - 1))
            print(register)
            break


if __name__ == '__main__':
    main()
