"""
Day8, license parsing
"""

import re
import sys


class Node(object):
    def __init__(self, children):
        self.num_children = children
        self.children = []
        self.num_meta = None
        self.meta = []

    def __str__(self):
        return 'children {}, metas {}'.format(self.num_children, self.num_meta)

    def value(self):
        if self.num_children == 0:
            return sum(self.meta)
        else:
            value = 0
            for meta in self.meta:
                try:
                    child = self.children[meta - 1]
                    value += child.value()
                except IndexError:
                    continue

            return value


def parse_node(data, nodes):
    num_children = int(data.pop(0))
    node = Node(num_children)

    node.num_meta = int(data.pop(0))

    nodes.append(node)

    for child in range(int(num_children)):
        node.children.append(parse_node(data, nodes))
    for meta in range(node.num_meta):
        node.meta.append(int(data.pop(0)))

    return node


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.read()
    else:
        values = sys.stdin.read()

    data = values.split(' ')
    nodes = []

    while data:
        parse_node(data, nodes)

    meta_sum = 0
    for node in nodes:
        meta_sum += sum(node.meta)

    print('meta sum: {}'.format(meta_sum))
    print('value for first node: {}'.format(nodes[0].value()))


if __name__ == '__main__':
    main()
