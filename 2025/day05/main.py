import sys

def part1(input: str) -> None:
    fresh_id_ranges = []
    available_ids = []
    with open(input, 'r') as file:
        available_id_line = False
        for line in file:
            if line.strip() == '':
                available_id_line = True
                continue

            if available_id_line:
                available_ids.append(int(line.strip()))
            else:
                min_id, max_id = line.strip().split('-')
                fresh_id_ranges.append((int(min_id), int(max_id)))

    result = 0
    for available_id in available_ids:
        for min_fresh_id, max_fresh_id in fresh_id_ranges:
            if min_fresh_id <= available_id <= max_fresh_id:
                result += 1
                break

    print(result)


def part2(input: str) -> None:
    fresh_id_ranges = []
    with open(input, 'r') as file:
        for line in file:
            if line.strip() == '':
                break

            min_id, max_id = line.strip().split('-')
            fresh_id_ranges.append([int(min_id), int(max_id)])

    fresh_id_ranges.sort(key=lambda x:x[0])

    merged = [fresh_id_ranges[0]]
    for min_fresh_id, max_fresh_id in fresh_id_ranges:
        if min_fresh_id <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], max_fresh_id)
        else:
            merged.append([min_fresh_id, max_fresh_id])

    result = 0
    for min_fresh_id, max_fresh_id in merged:
        result += max_fresh_id - min_fresh_id + 1

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


