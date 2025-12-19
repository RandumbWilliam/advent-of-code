import sys

def part1(input: str) -> None:
    grid = []
    with open(input, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

    adj_dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    result = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == '.':
                continue

            adj_rolls = 0
            for dx, dy in adj_dirs:
                x, y = i + dx, j + dy
                if x < 0 or x >= len(grid) or y < 0 or y >= len(row):
                    continue
                
                if grid[x][y] == '@':
                    adj_rolls += 1

            if adj_rolls < 4:
                result += 1

    print(result)

def part2(input: str) -> None:
    grid = []
    with open(input, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

    adj_dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    result = 0
    while True:
        rolls = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == '.':
                    continue

                adj_rolls = 0
                for dx, dy in adj_dirs:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(row):
                        continue
                    
                    if grid[x][y] == '@':
                        adj_rolls += 1

                if adj_rolls < 4:
                    grid[i][j] = '.'
                    rolls += 1

        result += rolls
        if rolls == 0:
            break

    print(result)


def usage():
    print("Usage: python3 main.py <part1|part2> <input.txt>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    part = sys.argv[1]

    if part not in ["part1", "part2"]:
        usage()

    input = sys.argv[2]

    if part == "part1":
        part1(input)

    if part == "part2":
        part2(input)

