def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line.strip()))
    return puzzle_input


def solve_part_1(subject_numbers):
    card = subject_numbers[0]
    door = subject_numbers[1]
    handshake = 1
    loopsize_card = 0
    loopsize_door = 0
    while handshake != card:
        loopsize_card += 1
        handshake *= 7
        handshake = handshake % 20201227

    handshake = 1
    while handshake != door:
        loopsize_door += 1
        handshake *= 7
        handshake = handshake % 20201227

    print("card: ", loopsize_card)
    print("door: ", loopsize_door)

    key = 1
    for i in range(loopsize_card):
        key *= door
        key = key % 20201227

    return key


def solve_part_2(puzzle_input):
    pass


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
