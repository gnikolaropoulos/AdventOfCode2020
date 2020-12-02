from itertools import combinations


def solve_part_1(puzzle_input):
    for a, b in combinations(puzzle_input, 2):
        if a + b == 2020:
            return a * b
    return ""


def solve_part_2(puzzle_input):
    for a, b, c in combinations(puzzle_input, 3):
        if a + b + c == 2020:
            return a * b * c
    return ""


def find_sum_of_two(sum_to_find, array_of_values):
    checked_numbers = {}
    for number in array_of_values:
        if sum_to_find - number in checked_numbers:
            return number, sum_to_find - number
        else:
            checked_numbers[number] = True


def elegantly_solve_part_1(puzzle_input):
    x, y = find_sum_of_two(2020, puzzle_input)
    return x * y


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")

    # more elegant solutions
    elegant_answer_1 = elegantly_solve_part_1(puzzle_input)
    print(f"Part 1 (elegant): {answer_1}")
