from library import io
from typing import List, AnyStr, Iterator


def part1(height_grid: List[List[int]]) -> int:
    horizontal_maxima = [max(_) for _ in height_grid]
    vertical_maxima = [max(_) for _ in map(list, zip(*height_grid))]

    visible_count = 0
    for x, row in enumerate(height_grid[1:-1]):
        for y, tree in enumerate(row[1:-1]):
            if tree <= horizontal_maxima[x+1] and tree <= vertical_maxima[y+1]:
                print(tree, x, row)
                visible_count += 1
    return visible_count


def part2():
    ...


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))

    print("Part 1:\n", part1(test_data), "\n")
    # print("Part 2:\n", part2(test_data), "\n")

