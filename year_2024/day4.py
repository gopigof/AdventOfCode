from http.cookiejar import cut_port_re
from turtledemo.penrose import start

from commons.reader import load_input_data, InputFileTypes


def part1(grid: list[str]):
    search_terms = {
        "X": "XMAS",
        "S": "SAMX"
    }
    occurrences = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in search_terms.keys():
                current_search_term = search_terms[grid[i][j]]
                # Check right
                if j + len(current_search_term) - 1 < len(grid[i]):
                    if ''.join(grid[i][j:j+len(current_search_term)]) == current_search_term:
                        occurrences += 1
                        print(i, j, "right", current_search_term)

                # Check down
                if i + len(current_search_term) - 1 < len(grid):
                    if ''.join([grid[x][j] for x in range(i, i+len(current_search_term))]) == current_search_term:
                        occurrences += 1
                        print(i, j, "down", current_search_term)


                # Check diagonal down-right
                if i + len(current_search_term) - 1 < len(grid) and j + len(current_search_term) - 1< len(grid[i]):
                    if ''.join(grid[x][y] for x, y in zip(range(i, i + 4), range(j, j + 4))) == current_search_term:
                        occurrences += 1
                        print(i, j, "down-right", current_search_term)


                # Check diagonal down-left
                if i + len(current_search_term) - 1 < len(grid) and len(current_search_term) - j >= 1:
                    if ''.join(grid[x][y] for x, y in zip(range(i, i + 4), range(j - 4, j))) == current_search_term:
                        occurrences += 1
                        print(i, j, "down-left", current_search_term)


    return occurrences


def part2(levels: list[list[int]]):
    ...


def main():
    input_lines = load_input_data(__file__, InputFileTypes.TEST)
    
    print(f"Part 1: {part1(input_lines)}")
    print(f"Part 2: {part2(input_lines)}")


if __name__ == '__main__':
    main()
