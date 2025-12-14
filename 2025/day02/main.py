import sys

def part1(input: str) -> None:
    file = open(input, 'r')
    id_ranges = file.read().split(',')

    result = 0
    for id_range in id_ranges:
        first_id, last_id = id_range.split('-')
        for id in range(int(first_id), int(last_id) + 1):
            str_id = str(id)
            str_id_length = len(str_id)
            if str_id_length % 2 == 0:
                split_index = str_id_length // 2
                if str_id[:split_index] == str_id[split_index:]:
                    result += id

    print(result)


def part2(input: str) -> None:
    file = open(input, 'r')
    id_ranges = file.read().split(',')

    result = 0
    for id_range in id_ranges:
        first_id, last_id = id_range.split('-')
        for id in range(int(first_id), int(last_id) + 1):
            str_id = str(id)
            str_id_length = len(str_id)

            valid = True
            for i in range(str_id_length // 2):
                i += 1
                if str_id_length % i == 0:
                    pattern = str_id[:i]
                    repeating = True
                    for j in range(0, str_id_length, i):
                        if pattern != str_id[j:j+i]:
                            repeating = False
                            break

                    if repeating:
                        valid = False
                        break

            if not valid:
                result += id

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


