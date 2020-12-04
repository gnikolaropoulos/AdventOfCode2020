from functools import reduce


def solve_part_1(puzzle_input):
    line_width = len(puzzle_input[0])
    position_x = 0
    number_of_trees = 0
    for line in puzzle_input:
        if line[position_x % line_width] == "#":
            number_of_trees += 1
        position_x += 3
    return number_of_trees


def solve_part_2(puzzle_input):
    line_width = len(puzzle_input[0])
    grid_height = len(puzzle_input)

    trees_per_pass = []
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        x = 0
        trees = 0
        for i in range(0, grid_height, down):
            if puzzle_input[i][x % line_width] == "#":
                trees += 1
            x += right

        trees_per_pass.append(trees)

    return reduce(lambda a, b: a * b, trees_per_pass)


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip())
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
