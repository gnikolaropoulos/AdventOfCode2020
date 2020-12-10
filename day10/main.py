def solve_part_1(joltages):
    joltages.sort()
    ones = 1
    threes = 1
    for i in range(len(joltages) - 1):
        diff = joltages[i + 1] - joltages[i]
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1

    return ones * threes


def solve_part_2(joltages):
    joltages.sort()
    combinations = [0]*len(joltages)
    for i in range(3):
        if joltages[i] <= 3:
            combinations[i] = 1
    for i in range(len(joltages)):
        for j in range(1, 4):
            if i + j < len(joltages):
                if joltages[i+j]-joltages[i] <= 3:
                    combinations[i+j] += combinations[i]
    return combinations[-1]

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

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
