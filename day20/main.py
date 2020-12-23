import math
from collections import Counter


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
    corner_tiles = set()
    for border, tile_ids in borders.items():
        if len(tile_ids) > 1:
            continue

        tile = tile_ids[0]
        if tile in edges and border != edges[tile][::-1]:
            corner_tiles.add(tile)
        else:
            edges[tile] = border

    product = 1
    for corner in list(corner_tiles):
        product *= corner

    return product


def solve_part_2(tiles):
    tile_sides = {}
    all_sides = Counter()
    tiles_by_num = {}
    for tile in tiles:
        tile_lines = [list(line) for line in tiles[tile]]
        tile_sides[tile] = Counter()
        for i in [0, -1]:
            side1 = tile_lines[i].copy()
            side2 = [line[i] for line in tile_lines]
            for c in [tile_sides[tile], all_sides]:
                c[tuple(side1.copy())] += 1
                c[tuple(side2.copy())] += 1
                c[tuple(reversed(side1.copy()))] += 1
                c[tuple(reversed(side2.copy()))] += 1
        tiles_by_num[tile] = tile_lines.copy()

    corner = None
    for tile_num, sides in tile_sides.items():
        num_unique = 0
        for side in sides:
            if all_sides[side] - sides[side] == 0:
                num_unique += 1
        if num_unique == 4:
            corner = tile_num
            break

    def rotate(lines):
        new_lines = []
        for col_i in range(len(lines)):
            new_lines.append([line[col_i] for line in reversed(lines)])
        return new_lines

    def flip(lines):
        for line in lines:
            line.reverse()

    size = int(math.sqrt(len(tiles_by_num)))
    tiles_by_num[corner].reverse()
    map = []
    for y in range(size):
        map.append([])
        for x in range(size):
            if x == 0 and y == 0:
                map[y].append(tiles_by_num.pop(corner))
                continue
            found = False
            for tile_num in tiles_by_num:
                for _ in range(2):
                    for _ in range(4):
                        tile = tiles_by_num[tile_num]
                        fits = True
                        if y != 0 and map[y - 1][x][-1] != tile[0]:
                            fits = False
                        if fits and x != 0 and [line[-1] for line in map[y][x - 1]] != [line[0] for line in tile]:
                            fits = False
                        if fits:
                            found = True
                            map[y].append(tiles_by_num.pop(tile_num))
                            break
                        else:
                            tiles_by_num[tile_num] = rotate(tiles_by_num[tile_num])
                    if found:
                        break
                    flip(tiles_by_num[tile_num])
                if found:
                    break
            if not found:
                print('Missing', x, y)

    tile_size = len(map[0][0]) - 2
    map_lines = [[] for _ in range(size * tile_size)]
    for tile_y, y_tiles in enumerate(map):
        y_offset = tile_size * tile_y
        for tile in y_tiles:
            for y, line in enumerate(tile[1:-1]):
                map_lines[y_offset + y].extend(line[1:-1])

    sea_monster = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   ",
                   ]

    num_mon = 0
    for _ in range(2):
        for _ in range(4):
            for mon_y in range(len(map_lines) - len(sea_monster)):
                for mon_x in range(len(map_lines[0]) - len(sea_monster[0])):
                    is_mon = True
                    for y, mon_line in enumerate(sea_monster):
                        for x, mon_char in enumerate(mon_line):
                            if mon_char == '#' and map_lines[mon_y + y][mon_x + x] != '#':
                                is_mon = False
                    if is_mon:
                        num_mon += 1
            if num_mon == 0:
                map_lines = rotate(map_lines)
            else:
                break
        if num_mon == 0:
            flip(map_lines)
        else:
            break

    mon_count = 0
    for line in sea_monster:
        mon_count += line.count('#')
    total_count = 0
    for line in map_lines:
        total_count += line.count('#')
    return total_count - mon_count * num_mon


def get_puzzle_input():
    tiles = {}
    with open("input.txt") as input_txt:
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
