# https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

from heapq import heappop, heappush, heapify
import sys

def distance(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2


def find_parent(parents, i):
    if parents[i] == i:
        return i

    parents[i] = find_parent(parents, parents[i])
    return parents[i]


def part1(input: str, connections: int) -> None:
    junction_boxes = []
    with open(input, 'r') as file:
        for line in file:
            junction_boxes.append(tuple(map(int, line.strip().split(','))))

    edges = []
    heapify(edges)

    for i in range(len(junction_boxes) - 1):
        for j in range(i + 1, len(junction_boxes)):
            p = junction_boxes[i]
            q = junction_boxes[j]
            heappush(edges, (distance(p, q), i, j))

    # junction box to parent junction box in the circuit
    parents = [i for i in range(len(junction_boxes))]

    for _ in range(connections):
        _, i, j = heappop(edges)

        pi = find_parent(parents, i)
        pj = find_parent(parents, j)

        if pi == pj:
            continue

        parents[pi] = pj

    circuit_sizes = [0] * len(junction_boxes)
    for box in range(len(junction_boxes)):
        root = find_parent(parents, box)
        circuit_sizes[root] += 1

    result = 1
    for circuit_size in sorted(circuit_sizes)[-3:]:
        result *= circuit_size

    print(result)


def part2(input: str) -> None:
    junction_boxes = []
    with open(input, 'r') as file:
        for line in file:
            junction_boxes.append(tuple(map(int, line.strip().split(','))))

    edges = []
    heapify(edges)

    for i in range(len(junction_boxes) - 1):
        for j in range(i + 1, len(junction_boxes)):
            p = junction_boxes[i]
            q = junction_boxes[j]
            heappush(edges, (distance(p, q), i, j))

    # junction box to parent junction box in the circuit
    parents = [i for i in range(len(junction_boxes))]

    result = 0

    circuits = len(junction_boxes)

    for _ in range(len(edges) - 1):
        _, i, j = heappop(edges)

        pi = find_parent(parents, i)
        pj = find_parent(parents, j)

        if pi == pj:
            continue

        parents[pi] = pj
        circuits -= 1
        if circuits == 1:
            result = junction_boxes[i][0] * junction_boxes[j][0]
            break

    print(result)


def usage():
    print("Usage: python3 main.py <part1|part2> <input.txt> <connections>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()

    part = sys.argv[1]

    if part not in ["part1", "part2"]:
        usage()

    input = sys.argv[2]

    connections = 0
    if part == "part1":
        connections = int(sys.argv[3])

    if part == "part1":
        part1(input, connections)

    if part == "part2":
        part2(input)

