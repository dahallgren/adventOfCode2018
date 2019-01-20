""""
Day7
"""

import re
import sys


PENALTY = 60
NUM_WORKERS = 5

class Worker(object):
    def __init__(self, node):
        self.node = node
        self.time = Worker.time_to_complete(node)

    @staticmethod
    def time_to_complete(char):
        return int(char.encode('hex'), 16) - 64 + PENALTY

    def tick(self):
        self.time -= 1
        return self.time


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as s:
            values = s.readlines()
    else:
        values = sys.stdin.readlines()

    graph = {}
    blocks = {}
    nodes = set()

    for value in values:
        match = re.match(r'Step (\w) must be finished before step (\w) can begin\.', value)

        val_first = match.groups()[0]
        val_second = match.groups()[1]

        graph.setdefault(val_first, []).append(val_second)
        blocks.setdefault(val_second, []).append(val_first)


        nodes.add(val_first)
        nodes.add(val_second)

    # for k,v in graph.iteritems():
    #    print(k, time_to_complete(k), v)
    # print(nodes)
    #
    # for k,v in blocks.iteritems():
    #     print(k, v)
    # print(nodes)

    # find root
    roots = sorted(nodes - set(blocks.keys()))
    walked = set()

    def is_runnable(node):
        blocking = blocks.get(node, [])
        return not any([x in nodes for x in blocking])

    queue = roots
    workers = []
    ticks = 0
    while queue or len(workers) > 0:
        runnable = sorted(filter(is_runnable, queue ))

        while runnable and len(workers) < NUM_WORKERS:
            node = runnable.pop(0)
            queue.remove(node)
            workers.append(Worker(node))

        next_nodes = []
        workers_done = []
        for worker in workers:
            worker.tick()
            if worker.time == 0:
                # Worker done!
                sys.stdout.write(worker.node)
                walked.add(worker.node)
                nodes.remove(worker.node)
                next_nodes.extend(graph.get(worker.node, []))
                workers_done.append(worker)

        for worker in workers_done:
            workers.remove(worker)

        queue.extend(next_nodes)
        queue = sorted(set(queue) - walked)

        ticks += 1

    print('')
    print(ticks)


if __name__ == '__main__':
    main()
