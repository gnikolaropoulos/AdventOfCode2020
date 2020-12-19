import re


def get_regexes(rules):
    def get_regex_str(rule_num):
        if isinstance(rules[rule_num], str):
            return rules[rule_num]
        else:
            sub_regexes = []
            for match in rules[rule_num]:
                sub_regexes.append(''.join([get_regex_str(option) for option in match]))
            return '(' + '|'.join(sub_regexes) + ')'

    return {i: re.compile('^' + get_regex_str(i) + '$') for i in rules.keys()}


def get_regexes_with_changes(rules):
    def get_regex_str(rule_num):
        if isinstance(rules[rule_num], str):
            return rules[rule_num]
        elif rule_num == 8:
            return '(' + get_regex_str(42) + ')+'
        elif rule_num == 11:
            forty_two, thirty_one = get_regex_str(42), get_regex_str(31)

            sub_regexes = []
            for i in range(1, 6):  # heuristic on how many cycles to expect
                sub_regexes.append(forty_two * i + thirty_one * i)
            return '(' + '|'.join(sub_regexes) + ')'
        else:
            sub_regexes = []
            for match in rules[rule_num]:
                sub_regexes.append(''.join([get_regex_str(option) for option in match]))
            return '(' + '|'.join(sub_regexes) + ')'

    return {i: re.compile('^' + get_regex_str(i) + '$') for i in rules.keys()}


def solve_part_1(rules, messages):
    regexes = get_regexes(rules)
    return sum(bool(regexes[0].match(m)) for m in messages)


def solve_part_2(rules, messages):
    regexes = get_regexes_with_changes(rules)
    return sum(bool(regexes[0].match(m)) for m in messages)


def get_puzzle_input():
    rules = {}
    messages = []
    rules_end = False
    with open("input.txt") as input_txt:
        for line in input_txt:
            if line.strip() and not rules_end:
                line = line.replace("\"", "")
                index = line.split(":")[0]
                rule_parts = line.split(":")[1].split("|")
                if len(rule_parts) == 1 and ("a" in rule_parts[0] or "b" in rule_parts[0]):
                    rules[int(index)] = rule_parts[0].strip()
                else:
                    rules[int(index)] = [[int(rule_id) for rule_id in rule.strip().split(" ")] for rule in rule_parts]
            elif not line.strip() and not rules_end:
                rules_end = True
            elif line.strip() and rules_end:
                messages.append(line.strip())

    return rules, messages


if __name__ == "__main__":
    rules, messages = get_puzzle_input()

    answer_1 = solve_part_1(rules, messages)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(rules, messages)
    print(f"Part 2: {answer_2}")
