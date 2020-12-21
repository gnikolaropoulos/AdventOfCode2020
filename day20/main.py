import math


def add_tile_id(borders, border, tile):
    temp = borders.get(border, [])
    temp.append(tile)
    borders[border] = temp


def get_borders(tiles):
    borders = {}
    for tile in tiles:
        add_tile_id(borders, tiles[tile][0], tile)
        add_tile_id(borders, tiles[tile][0][::-1], tile)

        add_tile_id(borders, tiles[tile][9], tile)
        add_tile_id(borders, tiles[tile][9][::-1], tile)

        left = ''.join(row[0] for row in tiles[tile])

        add_tile_id(borders, left, tile)
        add_tile_id(borders, left[::-1], tile)

        right = ''.join(row[-1] for row in tiles[tile])

        add_tile_id(borders, right, tile)
        add_tile_id(borders, right[::-1], tile)

    return borders


def solve_part_1(tiles):
    borders = get_borders(tiles)
    edges = {}
    coner_tiles = set()
    for border, tile_ids in borders.items():
        if len(tile_ids) > 1:
            continue

        tile = tile_ids[0]
        if tile in edges and border != edges[tile][::-1]:
            coner_tiles.add(tile)
        else:
            edges[tile] = border

    product = 1
    for corner in list(coner_tiles):
        product *= corner

    return product


def solve_part_2(puzzle_input):
    pass


def get_puzzle_input():
    tiles = {}
    with open("testinput.txt") as input_txt:
        tile_id = 0
        for line in input_txt:
            if "Tile" in line:
                tile_id = line.strip().split(' ')[1][:-1]
                tiles[int(tile_id)] = []
            else:
                if line.strip():
                    tiles[int(tile_id)].append(line.strip())
    return tiles

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
