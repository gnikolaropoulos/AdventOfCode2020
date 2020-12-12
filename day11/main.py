import copy

grid_rows = 99
grid_columns = 90


def arrange(i, j, grid, newgrid, steps_allowed, occupied_seats_limit):
    empty_seats_around = 0
    # look up
    next_row = i - 1
    while (
        0 <= next_row < grid_rows
        and grid[next_row][j] == "."
        and abs(next_row - i) < steps_allowed
    ):
        next_row -= 1
    if 0 <= next_row < grid_rows and grid[next_row][j] == "#":
        empty_seats_around += 1

    # look down
    next_row = i + 1
    while (
        0 <= next_row < grid_rows
        and grid[next_row][j] == "."
        and abs(next_row - i) < steps_allowed
    ):
        next_row += 1
    if 0 <= next_row < grid_rows and grid[next_row][j] == "#":
        empty_seats_around += 1

    # look left
    next_column = j - 1
    while (
        0 <= next_column < grid_columns
        and grid[i][next_column] == "."
        and abs(next_column - j) < steps_allowed
    ):
        next_column -= 1
    if 0 <= next_column < grid_columns and grid[i][next_column] == "#":
        empty_seats_around += 1

    # look right
    next_column = j + 1
    while (
        0 <= next_column < grid_columns
        and grid[i][next_column] == "."
        and abs(next_column - j) < steps_allowed
    ):
        next_column += 1
    if 0 <= next_column < grid_columns and grid[i][next_column] == "#":
        empty_seats_around += 1

    # look up and left
    next_row = i - 1
    next_column = j - 1
    while (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "."
        and abs(next_row - 1) < steps_allowed
        and abs(next_column - 1) < steps_allowed
    ):
        next_row -= 1
        next_column -= 1
    if (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "#"
    ):
        empty_seats_around += 1

    # look up and right
    next_row = i - 1
    next_column = j + 1
    while (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "."
        and abs(next_row - 1) < steps_allowed
        and abs(next_column - 1) < steps_allowed
    ):
        next_row -= 1
        next_column += 1
    if (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "#"
    ):
        empty_seats_around += 1

    # look down and left
    next_row = i + 1
    next_column = j - 1
    while (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "."
        and abs(next_row - 1) < steps_allowed
        and abs(next_column - 1) < steps_allowed
    ):
        next_row += 1
        next_column -= 1
    if (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "#"
    ):
        empty_seats_around += 1

    # look down and right
    next_row = i + 1
    next_column = j + 1
    while (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "."
        and abs(next_row - 1) < steps_allowed
        and abs(next_column - 1) < steps_allowed
    ):
        next_row += 1
        next_column += 1
    if (
        0 <= next_row < grid_rows
        and 0 <= next_column < grid_columns
        and grid[next_row][next_column] == "#"
    ):
        empty_seats_around += 1

    if grid[i][j] == "L" and empty_seats_around == 0:
        newgrid[i][j] = "#"
    elif grid[i][j] == "#" and empty_seats_around >= occupied_seats_limit:
        newgrid[i][j] = "L"
    else:
        newgrid[i][j] = grid[i][j]


def count_occupied_seats(newgrid):
    count = 0
    for i in range(grid_rows):
        for j in range(grid_columns):
            if newgrid[i][j] == "#":
                count += 1
    return count


def pretty_print(grid):
    for i in range(grid_columns):
        print(grid[i])
    print("\n\n")


def solve_part_1(grid):
    newgrid = [[""] * grid_columns for _ in range(grid_rows)]
    while True:
        for i in range(grid_rows):
            for j in range(grid_columns):
                if grid[i][j] != ".":
                    arrange(i, j, grid, newgrid, 1, 4)
                else:
                    newgrid[i][j] = grid[i][j]
        # pretty_print(newgrid)
        if grid == newgrid:
            break
        grid = copy.deepcopy(newgrid)
        newgrid = [[""] * grid_columns for _ in range(grid_rows)]

    return count_occupied_seats(newgrid)


def solve_part_2(grid):
    newgrid = [[""] * grid_columns for _ in range(grid_rows)]
    while True:
        for i in range(grid_rows):
            for j in range(grid_columns):
                if grid[i][j] != ".":
                    arrange(i, j, grid, newgrid, max(grid_rows, grid_columns), 5)
                else:
                    newgrid[i][j] = grid[i][j]
        # pretty_print(newgrid)
        if grid == newgrid:
            break
        grid = copy.deepcopy(newgrid)
        newgrid = [[""] * grid_columns for _ in range(grid_rows)]

    return count_occupied_seats(newgrid)


def get_puzzle_input():
    puzzle_input = [[""] * grid_columns for _ in range(grid_rows)]
    i = 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            j = 0
            for seat in line.strip():
                puzzle_input[i][j] = seat
                j += 1
            i += 1
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
