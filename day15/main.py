def solve_part_1(puzzle_input, limit):
    spoken_numbers = {}
    numbers = puzzle_input.split(",")
    for index, number in enumerate(numbers):
        spoken_numbers[int(number)] = [index+1]
    last_number_spoken = numbers[-1]
    i = len(numbers) + 1
    while i <= limit:
        if last_number_spoken in spoken_numbers.keys() and len(spoken_numbers[last_number_spoken]) > 1:
            first_appearance = spoken_numbers[last_number_spoken][-2]
            last_number_spoken = i-1 - first_appearance
            if last_number_spoken in spoken_numbers.keys():
                spoken_numbers[last_number_spoken].append(i)
            else:
                spoken_numbers[last_number_spoken] = [i]
        else:
            last_number_spoken = 0
            spoken_numbers[last_number_spoken].append(i)
        i += 1
    return last_number_spoken


def solve_part_2(puzzle_input, limit):
    return solve_part_1(puzzle_input, limit)


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input = line.strip()
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input, 2020)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input, 30000000)
    print(f"Part 2: {answer_2}")
