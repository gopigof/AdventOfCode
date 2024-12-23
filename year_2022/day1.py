from library import io
from typing import List


def part1(calories_list: str, top: int) -> int:
    """
    Find max group of cal sums
    """
    cals = calories_list.strip().split('\n')
    cals_count = []
    tmp_cals = 0
    for cal in cals:
        if cal != "":
            tmp_cals += int(cal)
        else:
            cals_count.append(tmp_cals)
            tmp_cals = 0
    cals_count.append(tmp_cals)
    return sum(sorted(cals_count, reverse=True)[:top])


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = io.read_text(test_fp)

    print(part1(test_data, top=1))
    print(part1(test_data, top=3))