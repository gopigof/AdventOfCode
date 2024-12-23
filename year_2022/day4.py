from library import io
from typing import List, AnyStr, Iterator, Iterable, Tuple


def process_input(assignment_pairs: List[AnyStr]) -> List[List[Tuple[int, int]]]:
    return [list(map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), pair.split(','))) for pair in assignment_pairs]


def part1(assignment_pairs: List[AnyStr]) -> int:
    split_ranges = process_input(assignment_pairs)
    return sum(
        [
            1 if range(max(x[0], y[0]), min(x[-1], y[-1]) + 1) in (range(x[0], x[1]+1), range(y[0], y[1] + 1)) else 0 for x, y in split_ranges
        ]
    )


def part2(assignment_pairs: List[AnyStr]) -> int:
    split_ranges = process_input(assignment_pairs)
    return sum(
        [
            (x[0] <= y[0] <= x[1]) or (y[0] <= x[0] <= y[1]) for x, y in split_ranges
        ]
    )


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))

    print("Part 1:\n", part1(test_data), "\n")
    print("Part 2:\n", part2(test_data), "\n")
