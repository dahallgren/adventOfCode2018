"""
Day 9, elves marble game
"""

import sys


class Marble(object):
    def __init__(self, value, prev=None, next=None):
        if prev:
            self.prev = prev
        else:
            self.prev = self

        if next:
            self.next = next
        else:
            self.next = self

        self.value = value

    def get_next(self, steps):
        ret = self
        for i in range(steps):
            ret = ret.next
        return ret

    def get_prev(self, steps):
        ret = self
        for i in range(steps):
            ret = ret.prev
        return ret

    def insert(self, value):
        new = Marble(value, self.prev, self)
        my_prev = self.prev
        my_prev.next = new
        self.prev = new
        return new

    def pop(self):
        prev = self.prev
        next = self.next
        prev.next = next
        next.prev = prev
        return self.value


def place_marble(current, number):
    item = current.get_next(2)
    return item.insert(number)


def main():
    players = int(sys.argv[1])
    last_marble = int(sys.argv[2])

    score = {}
    first = Marble(0)
    current = first

    current_player = 0
    for marble_value in range(1, last_marble+1):

        if marble_value % 10000 == 0:
            print(marble_value)
        current_player = (current_player + 1) % players
        if current_player == 0:
            current_player = players

        if marble_value % 23 == 0:
            # score!
            pop_marble = current.get_prev(7)
            p_score = score.get(current_player, 0)
            score[current_player] = p_score + marble_value + pop_marble.pop()
            current = pop_marble.get_next(1)
        else:
            current = current.get_next(2)
            current = current.insert(marble_value)

    score_board = sorted(zip(score.values(), score.keys()), reverse=True)
    print(score_board[0])


if __name__ == '__main__':
    main()
