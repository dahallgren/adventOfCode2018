import re
import sys
import copy

right_dir_next = {
    '-': '>',
    '\\': 'v',
    '/': '^',
    '+': 43,
    'left': '^',
    'straight': '>',
    'right': 'v'
}

left_dir_next = {
    '-': '<',
    '\\': '^',
    '/': 'v',
    '+': 43,
    'left': 'v',
    'straight': '<',
    'right': '^'
}

up_dir_next = {
    '|': '^',
    '\\': '<',
    '/': '>',
    '+': 43,
    'left': '<',
    'straight': '^',
    'right': '>'

}

down_dir_next = {
    '|': 'v',
    '\\': '>',
    '/': '<',
    '+': 43,
    'left': '>',
    'straight': 'v',
    'right': '<'

}

next_map = {
    '>': (right_dir_next, 0, 1),
    '<': (left_dir_next, 0, -1),
    '^': (up_dir_next, -1, 0),
    'v': (down_dir_next, 1, 0)
}

next_choice = {
    'left' : 'straight',
    'straight': 'right',
    'right': 'left'
}

track_map = []

class Crash(Exception):
    def __init__(self, message, y, x, track):
        # Call the base class constructor with the parameters it needs
        super(Crash, self).__init__(message)

        # Now for your custom code...
        self.y = y
        self.x = x
        self.track = track

class Cart(object):
    def __init__(self, direction, x, y):
        self.dir = direction
        self.x = x
        self.y = y
        self.track = '#'
        self.next_choice = 'left'

    def tick(self):
        next_dir_map, dy, dx = next_map[self.dir]
        next_track = track_map[self.y + dy][self.x + dx]
        try:
            next_dir = next_dir_map[next_track]
        except KeyError:
            track_map[self.y][self.x] = self.track
            self.x += dx
            self.y += dy
            raise Crash('Collision at x,y {},{} ({})'.format(self.x, self.y, next_track), self.y, self.x, next_track)
        if next_dir == 43:
            next_dir = next_dir_map[self.next_choice]
            self.next_choice = next_choice[self.next_choice]

        track_map[self.y][self.x] = self.track
        self.track = next_track
        self.x += dx
        self.y += dy
        self.dir = next_dir
        track_map[self.y][self.x] = self.dir


    def analyze_initial_track(self):
        if self.dir == '>':
            if track_map[self.y][self.x-1] in ('-', '+'):
                if track_map[self.y][self.x+1] in ('-', '+', '/', '\\'):
                    self.track = '-'
                else:
                    raise Exception('huh')
        elif self.dir == '<':
            if track_map[self.y][self.x+1] in ('-', '+', '/'):
                if track_map[self.y][self.x - 1] in ('-', '+', '/', '\\'):
                    self.track = '-'
                else:
                    raise Exception('huh')
        elif self.dir == '^':
            if track_map[self.y + 1][self.x] in ('|', '+'):
                if track_map[self.y - 1][self.x] in ('|', '+', '/', '\\'):
                    self.track = '|'
                else:
                    raise Exception('huh')
        elif self.dir == 'v':
            if track_map[self.y - 1][self.x] in ('|', '+'):
                if track_map[self.y + 1][self.x] in ('|', '+', '/', '\\'):
                    self.track = '|'
                else:
                    raise Exception('huh')


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()

    global track_map
    carts = []
    for y, line in enumerate(values):
        line = line.rstrip('\n')
        track_map.append(list(line))
        for x, track in enumerate(list(line)):
            if track in ('<', '>', '^', 'v'):
                print('new cart at y,x {},{}, dir {}'.format(y,x, track))
                carts.append(Cart(track, x, y))

    for cart in carts:
        cart.analyze_initial_track()

    ticks = 0
    del_x = None
    del_y = None
    print('Carts: {}'.format(len(carts)))
    while len(carts) > 1:
        #for line in track_map:
        #    print(''.join(line))

        if del_x:
            found = None
            for cart in carts:
                if cart.x == del_x and cart.y == del_y:
                    found = cart
                    break

            try:
                track_map[del_y][del_x] = found.track
            except AttributeError:
                for y, line in enumerate(track_map):
                    print('{:3} {}'.format(y, ''.join(line)))
                for cart in carts:
                    print('cart x,y {},{}'.format(cart.x, cart.y))
                raise

            carts.remove(found)
            print('Carts: {}'.format(len(carts)))

            del_x = None
            del_y = None
            continue

        iter_carts = copy.copy(carts)
        for cart in sorted(iter_carts, key= lambda c: (c.y, c.x)):
            if cart.x == del_x and cart.y == del_y:
                print('skip at {},{}'.format(del_x, del_y))
                continue
            try:
                cart.tick()
            except Crash as e:
                print(e.message)
                carts.remove(cart)
                del_x = e.x
                del_y = e.y
                # Uncomment this for part1
                # raise

        ticks += 1

        # print(ticks)


    last_cart = carts[0]
    print('cart x,y {},{}'.format(last_cart.x, last_cart.y))


if __name__ == '__main__':
    main()
