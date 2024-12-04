from collections import Counter

def part1(right, left):
    right.sort()
    left.sort()

    return sum([abs(i-j) for i,j in zip(right, left)])


def part2(right, left):
    left_counter = Counter(left)
    similarity = 0
    for num in right:
        similarity += num * left_counter[num]
    return similarity


def main():
    with open("data/year_2024/data/day1_input.txt") as f:
        data = f.read()
    num_list = [i.split() for i in data.split("\n") if i]
    right, left = [], []
    for i in num_list:
        right.append(int(i[0]))
        left.append(int(i[1]))

    print(f"Part1: {part1(right, left)}")
    print(f"Part2: {part2(right, left)}")


if __name__ == '__main__':
    main()
