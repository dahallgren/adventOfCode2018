import re
import sys
import copy

def main():

#     initial_state = '#..#.#..##......###...###'
#     unparsed_rules =\
# """...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #"""

    initial_state = "##..#..##....#..#..#..##.#.###.######..#..###.#.#..##.###.#.##..###..#.#..#.##.##..###.#.#...#.##.."

    unparsed_rules=\
"""##### => #
##.## => #
..##. => .
..#.# => .
..### => #
#..## => #
.#.#. => #
#.#.# => #
#.##. => .
####. => .
#..#. => #
..#.. => .
.#### => .
##.#. => #
#...# => .
.##.# => #
#.### => .
.#..# => #
.#... => #
.##.. => #
.###. => .
#.... => .
###.. => .
##..# => .
...## => #
##... => .
..... => .
....# => .
###.# => #
#.#.. => .
.#.## => #
...#. => ."""


    rules = dict()
    for line in unparsed_rules.split('\n'):
        rules[line[:5]] = line[-1]

    initial_state = '...' + initial_state + '...'

    pot_zero = 3

    def next_gen(state, pot_zero):
        num_pots = len(state)
        new_state = copy.copy(state)
        for i in range(num_pots-4):
            pot = i + 2
            current = ''.join(state[pot-2:pot+3])

            try:
                new_state[pot] = rules[current]
            except KeyError:
                new_state[pot] = '.'

        if '#' in ''.join(new_state[:3]):
            # print('prepend pots')
            new_state = ['.', '.', '.'] + new_state
            pot_zero += 3

        if '#' in ''.join(new_state[-3:]):
            # print('append pots')
            new_state = new_state + ['.', '.', '.']

        if ''.join(new_state[:5]).startswith('.....'):
            new_state = new_state[2:]
            pot_zero -=2




        return new_state, pot_zero

    state = list(initial_state)
    print(0, ''.join(state))
    total = 0
    for i in xrange(1, 50000000001):

        state, pot_zero = next_gen(state, pot_zero)
        total = 0
        for j in range(len(state)):
            if state[j] == '#':
                total += j - pot_zero

        # if i > 10:
        if i % 500 == 0:
             print(i, total)

    total = 0
    for i in range(len(state)):
        if state[i] == '#':
            total += i - pot_zero

    print(''.join(state))
    print(total)



if __name__ == '__main__':
    main()
