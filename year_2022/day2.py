from library import io
from typing import List, AnyStr, Iterator


GUIDE_MAPPING = dict((j, i-3) if i >= 3 else (j, i) for i, j in enumerate('ABCXYZ'))
SCORE_MATRIX = [[3, 1, 0], [1, 3, 2], [0, 2, 3]]
INVERSE_SCORE_MATRIX = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]


def rps_comparator(hand1: int, hand2: int) -> int:
    winner = SCORE_MATRIX[hand1][hand2]
    score = hand2 + 1
    if winner != hand1:
        score += 6 if winner == hand2 else winner
    return score


def inverse_rps_comparator(hand1: int, result: int) -> int:
    hand2 = INVERSE_SCORE_MATRIX[hand1][result]
    return hand2 + result*3 + 1


def part1(guide: List[AnyStr]) -> int:
    return sum([rps_comparator(*map(lambda x: GUIDE_MAPPING[x], i.split(" "))) for i in guide])


def part2(guide: List[AnyStr]) -> int:
    return sum([inverse_rps_comparator(*map(lambda x: GUIDE_MAPPING[x], i.split(" "))) for i in guide])


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp))

    print("Part 1:\n", part1(test_data), "\n")
    print("Part 2:\n", part2(test_data), "\n")
