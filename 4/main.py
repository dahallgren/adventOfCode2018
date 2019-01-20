import re
import sys

from collections import Counter


def main(args):
    with open(args, 'r') as s:
        values = s.readlines()

    current_id = None
    start_sleep = 0
    total_sleep = {}
    sleep_histo = {}
    for value in values:
        match = re.match(r'\[(?P<datetime>.*)\] Guard #(?P<id>\d+) begins shift', value)
        if match:
            current_id = match.groupdict()['id']
            continue

        match = re.match(r'\[(?P<datetime>.*)\] falls asleep', value)
        if match:
            start_sleep = int(match.groupdict()['datetime'].split(':')[1])
            continue

        match = re.match(r'\[(?P<datetime>.*)\] wakes up', value)
        if match:
            end_sleep = int(match.groupdict()['datetime'].split(':')[1])
            so_far = total_sleep.get(current_id, 0)
            total_sleep[current_id] = so_far + (end_sleep-start_sleep)
            for minute in range(start_sleep, end_sleep):
                sleep_histo.setdefault(current_id, []).append(minute)
            continue

    total_minutes, guard = max(zip(total_sleep.values(), total_sleep.keys()))
    histo = Counter(sleep_histo[guard])
    (min_sleep, minute) = max(zip(histo.values(), histo.keys()))

    print('Strategy 1: Choose guard {} minute {}, slept for {} minutes ### answer: {}'
          .format(guard, minute, total_minutes, int(guard)*int(minute)))

    max_length = 0
    for k,v in sleep_histo.iteritems():
        histo = Counter(v)
        length, minute = max(zip(histo.values(), histo.keys()))
        if length > max_length:
            guard = k
            max_length = length
            print('Strategy 2: Guard {}, minute {}, length {} ### {}'
                  .format(guard, minute, length, int(guard) * int(minute)))


if __name__ == '__main__':
    main(sys.argv[1])
