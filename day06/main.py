def get_puzzle_input():
    group_answers = []
    groups = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if not line.strip():
                groups.append(group_answers)
                group_answers = []
            else:
                group_answers.append(line.strip())

        groups.append(group_answers)
    return groups


def solve_part_1(groups):
    count = 0
    for group in groups:
        answers = {}
        for line in group:
            for answer in line:
                answers[answer] = 1
        count += len(answers)
    return count


def solve_part_2(groups):
    total_count = 0
    for group in groups:
        persons_count = 0
        answers = {}
        for line in group:
            persons_count += 1
            for answer in line:
                answers[answer] = answers.get(answer, 0) + 1
        total_count += sum(1 for key in answers.keys() if answers[key] == persons_count)
    return total_count


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
