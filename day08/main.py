import enum
import re

acc_re = re.compile("^acc ([+-]\d+)$")
jmp_re = re.compile("^jmp ([+-]\d+)$")
nop_re = re.compile("^nop ([+-]\d+)$")


def run(instructions):
    accumulator = 0
    executed_instructions = []
    i = 0
    while i not in executed_instructions:
        if i == len(instructions):
            return accumulator, "finished"
        executed_instructions.append(i)
        match = acc_re.match(instructions[i])
        if match:
            accumulator += int(match.group(1))
            i += 1
            continue
        match = jmp_re.match(instructions[i])
        if match:
            i += int(match.group(1))
            continue
        if "nop" in instructions[i]:
            i += 1
            continue

    return accumulator, "inloop"


def solve_part_1(puzzle_input):
    accumulator, state = run(puzzle_input)
    return accumulator


def solve_part_2(puzzle_input):
    for i in range(len(puzzle_input)):
        match = acc_re.match(puzzle_input[i])
        if match:
            continue
        match = nop_re.match(puzzle_input[i])
        if match:
            puzzle_input[i] = "jmp " + match.group(1)
            accumulator, state = run(puzzle_input)
            if state == "finished":
                return accumulator
            puzzle_input[i] = "nop " + match.group(1)
            continue
        match = jmp_re.match(puzzle_input[i])
        if match:
            puzzle_input[i] = "nop " + match.group(1)
            accumulator, state = run(puzzle_input)
            if state == "finished":
                return accumulator
            puzzle_input[i] = "jmp " + match.group(1)

    return accumulator


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
