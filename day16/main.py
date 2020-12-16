import re
from collections import defaultdict

double_field_re = re.compile("^([\w\s]+):\s(\d+)-(\d+) or (\d+)\-(\d+)$")
field_re = re.compile("^([\w\s]+):\s(\d+)-(\d+)$")


def solve_part_1(fields, tickets):
    out_of_limits = []
    for ticket in tickets:
        numbers = [int(n) for n in ticket.split(",")]
        for number in numbers:
            found = False
            for field in fields:
                limits = fields[field]
                if len(fields[field]) == 4:
                    if limits[-4] <= number <= limits[-3] or limits[-2] <= number <= limits[-1]:
                        found = True
                elif len(fields[field]) == 2:
                    if limits[-2] <= number <= limits[-1]:
                        found = True
            if not found:
                out_of_limits.append(number)
    return sum(out_of_limits)


def solve_part_2(fields,myticket,tickets):
    valid_tickets = []
    for ticket in tickets:
        all_found = True
        numbers = [int(n) for n in ticket.split(",")]
        for number in numbers:
            found = False
            for field in fields:
                limits = fields[field]
                if len(fields[field]) == 4:
                    if limits[-4] <= number <= limits[-3] or limits[-2] <= number <= limits[-1]:
                        found = True
                elif len(fields[field]) == 2:
                    if limits[-2] <= number <= limits[-1]:
                        found = True
            if not found:
                all_found = False
        if all_found:
            valid_tickets.append(ticket)
    valid_fields = defaultdict(set)

    for field in fields.keys():
        valid_fields[field] = set({x for x in range(len(fields.keys()))})

    for index in range(len(fields.keys())):
        for name in fields.keys():
            for ticket in valid_tickets:
                numbers = [int(n) for n in ticket.split(",")]
                number = numbers[index]
                limits = fields[name]
                if len(limits) == 4:
                    if not (limits[-4] <= number <= limits[-3] or limits[-2] <= number <= limits[-1]):
                        valid_fields[name].remove(index)
                        break
                elif len(limits) == 2:
                    if not limits[-2] <= number <= limits[-1]:
                        valid_fields[name].remove(index)
                        break
    decided = set()

    while any(len(indices) > 1 for indices in valid_fields.values()):
        for k, v in valid_fields.items():
            if len(v - decided) == 1:
                valid_fields[k] -= decided
                decided |= valid_fields[k]

    departures = [position for k, v in valid_fields.items() for position in v if 'departure' in k]

    val = 1
    for dep in departures:
        val *= int(myticket[dep])

    return val


def get_puzzle_input():
    fields = defaultdict(list)
    myticket = []
    tickets = []
    is_mine = False
    with open("input.txt") as input_txt:
        for line in input_txt:
            if double_field_re.match(line.strip()):
                match = double_field_re.match(line.strip())
                fields[match.group(1)] = [int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5))]
            elif field_re.match(line.strip()):
                match = field_re.match(line.strip())
                fields[match.groups(1)] = [match.groups(2), match.groups(3)]
            elif "your ticket" in line.strip():
                is_mine = True
            elif "nearby" in line.strip():
                continue
            elif is_mine:
                myticket = line.strip().split(",")
                is_mine = False
            else:
                if line.strip():
                    tickets.append(line.strip())
    return fields, myticket, tickets



if __name__ == "__main__":
    fields, myticket, tickets = get_puzzle_input()

    answer_1 = solve_part_1(fields, tickets)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(fields,myticket,tickets)
    print(f"Part 2: {answer_2}")