def solve_part_1(timestamp, buses):
    waiting = 0
    while True:
        for buss in buses.values():
            if buss != 0:
                if (timestamp+waiting) % buss == 0:
                    return waiting * buss
        waiting += 1


def solve_part_2(buses):
    time = 0
    jump = buses[0]
    for timestamp, next_buss in buses.items():
        if next_buss == jump:
            continue
        tries = 0

        while (time + jump * tries + timestamp) % next_buss != 0:
            tries += 1

        time += tries * jump
        jump *= next_buss

    return time




def get_puzzle_input():
    timestamp = 0
    buses = {}
    i = 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            if i == 0:
                timestamp = int(line.strip())
                i += 1
            else:
                for buss in line.strip().split(","):
                    # if buss == "x":
                    #     busses[i] = 0
                    if buss.isdigit():
                        buses[i-1] = int(buss)
                      #  busses.append(int(buss))
                    i += 1
    return timestamp, buses


if __name__ == "__main__":
    timestamp, puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(timestamp, puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
