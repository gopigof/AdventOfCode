from library import io, strings
from typing import List, AnyStr, Iterator
from collections import namedtuple
from copy import deepcopy

Instruction = namedtuple("Instruction", ["quantity", "source", "destination"])


def process_input(input_: List[AnyStr]) -> (List[List[AnyStr]], List[Instruction]):
    starting_stack, instructions = input_[:input_.index('')], input_[input_.index('')+1:]
    stack = [[] for _ in range(11)]
    for item in starting_stack:
        for idx, i in enumerate(item):
            if i.isupper():
                stack[(idx - 1) // 3].append(i)     # Inspired from Discord

    processed_instructions = [Instruction(*map(int, string_processing.multi_replace(i, ["move", "from", "to"]))) for i in instructions]
    return [_[::-1] for _ in stack if _], processed_instructions


def part1(stack: List[List[AnyStr]], procedure: List[Instruction]) -> AnyStr:
    for proc in procedure:
        # print(proc, stack)
        for _ in range(proc.quantity):
            stack[proc.destination - 1].append(stack[proc.source - 1].pop())
    return ''.join(i[-1] for i in stack)


def part2(stack: List[List[AnyStr]], procedure: List[Instruction]) -> AnyStr:
    for proc in procedure:
        stack[proc.destination - 1].extend(stack[proc.source - 1][-1 * proc.quantity:])
        del stack[proc.source - 1][-1 * proc.quantity:]
    return ''.join(i[-1] for i in stack)


if __name__ == '__main__':
    test_fp = io.load_file_path(__file__)
    test_data = list(io.read_split_lines(test_fp, False))
    initial_stack, procedure_ = process_input(test_data)

    print("Part 1:\n", part1(deepcopy(initial_stack), deepcopy(procedure_)), "\n")
    print("Part 2:\n", part2(initial_stack[:], procedure_), "\n")
