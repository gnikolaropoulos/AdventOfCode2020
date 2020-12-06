import re


def solve_part_1(passports):
    valid_passports_count = 0
    valid_fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    for passport in passports:
        valid_fields_count = 0
        for line in passport:
            for fields in line:
                field, value = fields.split(":")
                if field in valid_fields:
                    valid_fields_count += 1
        if valid_fields_count == 7:
            valid_passports_count += 1
    return valid_passports_count


def solve_part_2(passports):
    valid_passports_count = 0
    for passport in passports:
        good = True
        valid_fields_count = 0
        for line in passport:
            for fields in line:
                field, value = fields.split(":")
                if field == 'byr':
                    valid_fields_count += 1
                    if len(value) != 4 or not 1920 <= int(value) <= 2002:
                        good = False
                if field == 'iyr':
                    valid_fields_count += 1
                    if len(value) != 4 or not 2010 <= int(value) <= 2020:
                        good = False
                if field == 'eyr':
                    valid_fields_count += 1
                    if len(value) != 4 or not 2020 <= int(value) <= 2030:
                        good = False
                if field == 'hgt':
                    valid_fields_count += 1
                    nums = ints(value)
                    cm = len(value) > 1 and value[-2:] == 'cm'
                    inch = len(value) > 1 and value[-2:] == 'in'

                    if not (cm or inch):
                        good = False

                    if cm and not 150 <= nums[0] <= 193:
                        good = False

                    if inch and not 59 <= nums[0] <= 76:
                        good = False
                if field == 'hcl':
                    valid_fields_count += 1
                    if len(value) != 7 or value[0] != '#' or any(c not in '0123456789abcdef' for c in value[1:]):
                        good = False
                if field == 'pid':
                    valid_fields_count += 1
                    if len(value) != 9 or any(c not in '0123456789' for c in value):
                        good = False
                if field == 'ecl':
                    valid_fields_count += 1
                    if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        good = False

        if good and valid_fields_count == 7:
            valid_passports_count += 1

    return valid_passports_count


def get_puzzle_input():
    passports = []
    passport = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if not line.strip():
                passports.append(passport)
                passport = []
            else:
                passport.append(line.split())

        passports.append(passport)
    return passports


def ints(line):
    pattern = re.compile(r'-?\d+')

    return [int(val) for val in re.findall(pattern, line) if val]


if __name__ == "__main__":
    passports = get_puzzle_input()

    answer_1 = solve_part_1(passports)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(passports)
    print(f"Part 2: {answer_2}")
