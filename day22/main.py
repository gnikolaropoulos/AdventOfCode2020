from collections import deque

def get_puzzle_input():
    start_deck = False
    player = 0
    decks = {}
    with open("input.txt") as input_txt:
        for line in input_txt:
            if "Player" in line.strip():
                start_deck = True
                decks[player] = []
            elif start_deck and line.strip():
                decks[player].append(int(line.strip()))
            else:
                player += 1
    return decks


def solve_part_1(decks):
    end = False
    while not end:
        player1 = decks[0][0]
        player2 = decks[1][0]
        if player1 > player2:
            decks[1] = decks[1][1:]
            decks[0] = decks[0][1:]
            decks[0].append(player1)
            decks[0].append(player2)
        if player2 > player1:
            decks[0] = decks[0][1:]
            decks[1] = decks[1][1:]
            decks[1].append(player2)
            decks[1].append(player1)
        if len(decks[0]) == 0 or len(decks[1]) == 0:
            end = True

    winner = 0
    if decks[1]:
        winner = 1

    return sum(card * (len(decks[winner]) - i) for i, card in enumerate(decks[winner]))


def play_recursive(player1, player2):
    rounds = set()

    def freeze(p1, p2):
        return tuple(p1), tuple(p2)

    while player1 and player2:
        game = freeze(player1, player2)
        if game in rounds:
            return True, player1
        rounds.add(game)

        player1_card = player1.popleft()
        player2_card = player2.popleft()
        if len(player1) >= player1_card and len(player2) >= player2_card:  # Recurse
            p1_subdeck = deque(list(player1)[:player1_card])
            p2_subdeck = deque(list(player2)[:player2_card])
            p1_win, _ = play_recursive(p1_subdeck, p2_subdeck)
        else:
            p1_win = player1_card > player2_card

        if p1_win:
            player1.append(player1_card)
            player1.append(player2_card)
        else:
            player2.append(player2_card)
            player2.append(player1_card)

    return bool(player1), player1 if player1 else player2


def solve_part_2(decks):
    player1 = deque(decks[0])
    player2 = deque(decks[1])

    _, winner_deck = play_recursive(player1, player2)
    return sum(card * (len(winner_deck) - i) for i, card in enumerate(winner_deck))


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
