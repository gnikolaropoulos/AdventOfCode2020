def solve_part_1(instructions):
    facing = "EAST"
    manhattan = [0, 0]
    for instruction in instructions:
        dir = instruction[0]
        units = int(instruction[1:])
        if dir == 'N':
            manhattan[1] += units
        if dir == 'S':
            manhattan[1] -= units
        if dir == 'E':
            manhattan[0] += units
        if dir == 'W':
            manhattan[0] -= units

        if facing == "EAST":
            if dir == "F":
                manhattan[0] += units
            elif dir == "R":
                if units == 90:
                    facing = "SOUTH"
                elif units == 180:
                    facing = "WEST"
                elif units == 270:
                    facing = "NORTH"
            elif dir == "L":
                if units == 90:
                    facing = "NORTH"
                elif units == 180:
                    facing = "WEST"
                elif units == 270:
                    facing = "SOUTH"
        elif facing == "WEST":
            if dir == "F":
                manhattan[0] -= units
            elif dir == "R":
                if units == 90:
                    facing = "NORTH"
                elif units == 180:
                    facing = "EAST"
                elif units == 270:
                    facing = "SOUTH"
            elif dir == "L":
                if units == 90:
                    facing = "SOUTH"
                elif units == 180:
                    facing = "EAST"
                elif units == 270:
                    facing = "NORTH"
        elif facing == "NORTH":
            if dir == "F":
                manhattan[1] += units
            elif dir == "R":
                if units == 90:
                    facing = "EAST"
                elif units == 180:
                    facing = "SOUTH"
                elif units == 270:
                    facing = "WEST"
            elif dir == "L":
                if units == 90:
                    facing = "WEST"
                elif units == 180:
                    facing = "SOUTH"
                elif units == 270:
                    facing = "EAST"
        elif facing == "SOUTH":
            if dir == "F":
                manhattan[1] -= units
            elif dir == "R":
                if units == 90:
                    facing = "WEST"
                elif units == 180:
                    facing = "NORTH"
                elif units == 270:
                    facing = "EAST"
            elif dir == "L":
                if units == 90:
                    facing = "EAST"
                elif units == 180:
                    facing = "NORTH"
                elif units == 270:
                    facing = "WEST"

    return abs(manhattan[0]) + abs(manhattan[1])


def solve_part_2(instructions):
    waypoint = [10, 1]
    manhattan = [0, 0]

    for instruction in instructions:
        dir = instruction[0]
        units = int(instruction[1:])

        if dir == 'N':
            waypoint[1] += units
        if dir == 'S':
            waypoint[1] -= units
        if dir == 'E':
            waypoint[0] += units
        if dir == 'W':
            waypoint[0] -= units
        if dir == 'L':
            if units == 90:
                waypoint[0], waypoint[1] = waypoint[1] * -1, waypoint[0]
            if units == 180:
                waypoint[0] = waypoint[0] * -1
                waypoint[1] = waypoint[1] * -1
            if units == 270:
                waypoint[0], waypoint[1] = waypoint[1], waypoint[0] * -1
        if dir == 'R':
            if units == 90:
                waypoint[0], waypoint[1] = waypoint[1], waypoint[0] * - 1
            if units == 180:
                waypoint[0] = waypoint[0] * -1
                waypoint[1] = waypoint[1] * -1
            if units == 270:
                waypoint[0], waypoint[1] = waypoint[1] * -1, waypoint[0]
        if dir == 'F':
            manhattan[1] += units * waypoint[1]
            manhattan[0] += units * waypoint[0]

        print(instruction, (manhattan[0], manhattan[1]))
    return abs(manhattan[0]) + abs(manhattan[1])


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
