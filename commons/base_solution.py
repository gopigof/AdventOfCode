from commons.reader import load_input_data, InputFileTypes


def part1(levels: list[list[int]]):
    ...


def part2(levels: list[list[int]]):
    ...


def main():
    input_lines = load_input_data(__file__, InputFileTypes.TEST)
    
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == '__main__':
    main()
