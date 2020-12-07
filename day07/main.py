import re

line_re = re.compile("^(.*)bags[ ]contain[ ](.*)[.]$")
bag_content_re = re.compile("([1-5])[ ]([^,.]+)bag[s]?[,.]")
search_color = "shiny gold"


def get_puzzle_input():
    all_bags = {}
    with open("input.txt") as input_txt:
        for line in input_txt:
            match = line_re.match(line)
            if match:
                bag_color = match.group(1).strip()
                all_bags[bag_color] = []
                for content_match in bag_content_re.finditer(line):
                    all_bags[bag_color].append({"amount": content_match.group(1).strip(),
                                                "bag_color": content_match.group(2).strip()})
    return all_bags


def can_contain_gold_bag(bag, all_bags):
    contains = False
    if bag == search_color:
        contains = False
    for content in all_bags[bag]:
        if content["bag_color"] == search_color:
            contains = True
        if can_contain_gold_bag(content["bag_color"], all_bags):
            contains = True

    return contains


def find_required_bags(gold_bag, puzzle_input):
    total_count = 0
    for content in gold_bag:
        total_count += int(content["amount"])
        total_count += total_count * find_required_bags(puzzle_input[content["bag_color"]], puzzle_input)
    return total_count


def solve_part_1(puzzle_input):
    total_count = 0
    for bag in puzzle_input:
        if can_contain_gold_bag(bag, puzzle_input):
            total_count += 1
    return total_count


def solve_part_2(puzzle_input):
    gold_bag = puzzle_input[search_color]
    return find_required_bags(gold_bag, puzzle_input)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
