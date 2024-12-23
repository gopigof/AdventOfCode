from library import io
from typing import List, AnyStr, Iterator
from functools import reduce


def calc_priority(*iterables) -> int:
    for elem in reduce(lambda x, y: set(x).intersection(y), iterables):
        return ord(elem) - (96 if elem.islower() else 38)


def part1(rucksacks: List[AnyStr]) -> int:
    return sum([calc_priority(i[:len(i)//2], i[len(i)//2:]) for i in rucksacks])


def part2(rucksacks: List[AnyStr]) -> int:
    return sum([calc_priority(*rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)])


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))

    print("Part 1:\n", part1(test_data), "\n")
    print("Part 2:\n", part2(test_data), "\n")
