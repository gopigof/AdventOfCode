from commons.reader import load_input_data, InputFileTypes
import re

def parse_mul(inst: str) -> int:
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0

    for n1, n2 in mul_pattern.findall(inst):
        result += int(n1) * int(n2)
    return result


def part1(instructions: list[str]):
    result = 0
    for instr in instructions:
        result += parse_mul(instr)
    return result


def part2(instructions: list[str]):
    activation_instr_pattern = r"(don't\(\))|(do\(\))"
    result = 0
    instr_activated = True
    for instr in instructions:
        for instr_chunk in re.split(activation_instr_pattern, instr):
            if instr_chunk == "do()":
                instr_activated = True
            elif instr_chunk == "don't()":
                instr_activated = False
            else:
                if instr_activated and instr_chunk:
                    result += parse_mul(instr_chunk)
    return result


def main():
    input_lines = load_input_data(__file__, InputFileTypes.INPUT)

    print(f"Part 1: {part1(input_lines)}")
    print(f"Part 2: {part2(input_lines)}")


if __name__ == '__main__':
    main()
