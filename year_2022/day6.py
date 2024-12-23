from library import io
from typing import List, AnyStr, Iterator
from library import iterables


def part1(datastream: AnyStr, window: int):
    for idx in range(len(datastream[:-1 * window + 1])):
        if not iterables.contains_duplicates(*datastream[idx:idx+window]):
            return idx + window
    return None


def part2():
    ...


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))

    print("Part 1:\n", part1(test_data[0], 4), "\n")
    print("Part 2:\n", part1(test_data[0], 14), "\n")
