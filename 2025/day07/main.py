from collections import defaultdict
import sys

def part1(input: str) -> None:
    beams = set()
    splitter_rows = []
    with open(input, 'r') as file:
        for line in file:
            splitters = set()
            for j, space in enumerate(line.strip()):
                if space == 'S':
                    beams.add(j)
                if space == '^':
                    splitters.add(j)

            splitter_rows.append((splitters))

    result = 0
    for splitters in splitter_rows:
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                result += 1
                new_beams.add(beam + 1)
                new_beams.add(beam - 1)
            else:
                new_beams.add(beam)

        beams = new_beams

    print(result)


def part2(input: str) -> None:
    beam = 0
    splitter_rows = []
    with open(input, 'r') as file:
        for line in file:
            splitters = set()
            for j, space in enumerate(line.strip()):
                if space == 'S':
                    beam = j
                if space == '^':
                    splitters.add(j)

            splitter_rows.append((splitters))

    # memo = {}
    # def timelines(beam, splitter_row_index):
    #     key = (beam, splitter_row_index)
    #
    #     if key in memo:
    #         return memo[key]
    #
    #     if splitter_row_index == len(splitter_rows) - 1:
    #         return 1
    #
    #     next_splitter_row_index = splitter_row_index + 1
    #     if beam in splitter_rows[splitter_row_index]:
    #         result = timelines(beam + 1, next_splitter_row_index) + timelines(beam - 1, next_splitter_row_index)
    #     else:
    #         result = timelines(beam, next_splitter_row_index)
    #
    #     memo[key] = result
    #     return result
    #
    # result = timelines(beam, 0)
    
    states = defaultdict(int)
    states[beam] = 1

    for splitters in splitter_rows:
        next_states = defaultdict(int)
        for beam, count in states.items():
            if beam in splitters:
                next_states[beam + 1] += count
                next_states[beam - 1] += count
            else:
                next_states[beam] += count

        states = next_states

    result = sum(states.values())

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



