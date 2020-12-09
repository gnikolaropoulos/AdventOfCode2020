def is_valid(number_to_match, preample):
    for i in range(len(preample)):
        for j in range(i + 1, len(preample)):
            if number_to_match == preample[i] + preample[j]:
                return True
    return False


def solve_part_1(puzzle_input):
    preample = puzzle_input[:25]
    for i in range(len(preample), len(puzzle_input)):
        number_to_match = puzzle_input[i]
        if not is_valid(number_to_match, preample):
            return number_to_match
        preample.append(number_to_match)
        preample = preample[-25:]
    return 0


def solve_part_2(puzzle_input, target):
    for i in range(len(puzzle_input)):
        numbers = []
        for j in range(i, len(puzzle_input)):
            numbers.append(puzzle_input[j])
            if sum(numbers) == target:
                return min(numbers) + max(numbers)
            if sum(numbers) > target:
                break

    return 0


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line.strip()))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input, answer_1)
    print(f"Part 2: {answer_2}")
