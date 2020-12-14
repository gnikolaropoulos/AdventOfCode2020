import re

memory_re = re.compile("^mem\[(\d+)\] = (\d+)$")


def mask_input(mask, number):
    result = ""
    binary_number = "{0:b}".format(number)
    digits_to_fill = len(mask) - len(binary_number)
    binary = "0" * digits_to_fill + binary_number

    for index, bit in enumerate(mask):
        if bit == "X":
            result += binary[index]
        else:
            result += mask[index]
    return result


def solve_part_1(puzzle_input):
    memory = {}
    mask = ""
    for i in range(len(puzzle_input)):
        if "mask" in puzzle_input[i]:
            mask = puzzle_input[i].split("=")[1].strip()
        else:
            match = memory_re.match(puzzle_input[i])
            memory_index = int(match.group(1))
            number = int(match.group(2))
            masked_number = mask_input(mask, number)
            memory[memory_index] = int(masked_number, 2)
    return sum(memory.values())


def get_masked_addresses(mask, address):
    binary_address = "{0:b}".format(address)
    digits_to_fill = len(mask) - len(binary_address)
    binary_address = list('0' * digits_to_fill + binary_address)

    addresses = []
    floatings = {}

    for index, bit in enumerate(mask):
        if bit == '1':
            binary_address[index] = '1'
        elif bit == 'X':
            floatings[index] = len(floatings)

    for binary_number in range(2 ** (len(floatings))):
        binary_number = "{0:b}".format(binary_number)
        binary_number = '0' * (len(floatings) - len(binary_number)) + binary_number
        variant = ""

        for pos, bit in enumerate(binary_address):
            if pos in floatings:
                variant += binary_number[floatings[pos]]
            else:
                variant += binary_address[pos]

        addresses.append(int(variant, 2))

    return addresses


def solve_part_2(puzzle_input):
    memory = {}
    mask = ""
    for i in range(len(puzzle_input)):
        if "mask" in puzzle_input[i]:
            mask = puzzle_input[i].split("=")[1].strip()
        else:
            match = memory_re.match(puzzle_input[i])
            number = int(match.group(2))
            for address in get_masked_addresses(mask, int(match.group(1))):
                memory[address] = number
    return sum(memory.values())


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
