def solve_part_1(puzzle_input):
    seat_ids = []
    for line in puzzle_input:
        start_row = 0
        end_row = 127
        start_col = 0
        end_col = 7
        # a better solution is....
        # rows = rows.replace("F", "0").replace("B", "1")
        # row_id = int(rows, 2)

        for i in range(7):
            if line[i] == "F":
                end_row = int((start_row + end_row) / 2)
            if line[i] == "B":
                start_row = int((start_row + end_row + 1) / 2)

        # a better solution is....
        # columns = columns.replace("L", "0").replace("R", "1")
        # col_id = int(columns, 2)

        for i in range(7, 10):
            if line[i] == "R":
                start_col = int((end_col + start_col + 1) / 2)
            if line[i] == "L":
                end_col = int((end_col + start_col) / 2)
        new_seat_id = start_row * 8 + start_col
        seat_ids.append(new_seat_id)

    return seat_ids


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip())
    return puzzle_input


def solve_part_2(puzzle_input):
    puzzle_input.sort()
    for i in range(len(puzzle_input) - 1):
        if (puzzle_input[i + 1] - puzzle_input[i]) == 2:
            return int((puzzle_input[i] + puzzle_input[i + 1]) / 2)
    return "not found"


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    seats = solve_part_1(puzzle_input)
    print(f"Part 1: {max(seats)}")

    answer_2 = solve_part_2(seats)
    print(f"Part 2: {answer_2}")
