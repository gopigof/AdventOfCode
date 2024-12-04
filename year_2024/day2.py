from commons.reader import load_input_data, InputFileTypes


def part1_alt(levels: list[list[int]]):
    num_safe_reports = 0
    for level in levels:
        num_increases = 0
        for r1, r2 in zip(level, level[1:]):
            if r2 > r1:
                num_increases += 1
            if not (1 <=abs(r2 - r1) <= 3):
                break
        else:
            if num_increases == 0 or num_increases == len(level)-1:
                num_safe_reports += 1
    return num_safe_reports


def part1(levels: list[list[int]]):
    num_safe_reports = 0
    for level in levels:
        lvl_diff = [r2 - r1 for r1, r2 in zip(level, level[1:])]
        first_sign = lvl_diff[0] > 0
        if all(1 <= abs(d) <= 3 for d in lvl_diff) and (first_sign == all(d > 0 for d in lvl_diff)):
            num_safe_reports += 1
    return num_safe_reports


def part2(levels: list[list[int]]):
    num_safe_reports = 0
    for level in levels:
        warning = 0
        lvl_diff = [r2 - r1 for r1, r2 in zip(level, level[1:])]

        diffs = [1 <= abs(d) <= 3 for d in lvl_diff]
        signs = [i >= 0 for i in lvl_diff]

        print(level, lvl_diff, diffs)

        if diffs.count(False) >= 1:
            print( "has too many bad diffs")
            warning += 1
        if min(signs.count(True), signs.count(False)) >= 2:
            print("has too many bad signs")
            warning += 1
        if warning <= 1:
            num_safe_reports += 1
        # if all(1 <= abs(d) <= 3 for d in lvl_diff) and (first_sign == all(d > 0 for d in lvl_diff)):
        #     num_safe_reports += 1
    return num_safe_reports


def main():
    input_lines = load_input_data(__file__, InputFileTypes.TEST)
    levels_int = [[int(j) for j in i.split()] for i in input_lines]

    print(f"Part 1: {part1(levels_int)}")
    print(f"Part 2: {part2(levels_int)}")


if __name__ == '__main__':
    main()
