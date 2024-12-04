from commons.reader import load_input_data, InputFileTypes


def part1(levels: list[list[int]]):
    ...


def main():
    input_lines = load_input_data(__file__, InputFileTypes.TEST)
    levels_int = [[int(j) for j in i.split()] for i in input_lines]

    print(f"Part 1: {part1(levels_int)}")

if __name__ == '__main__':
    main()
