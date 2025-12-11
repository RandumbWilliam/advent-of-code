import sys
from collections import deque


class Advent:
    def __init__(self, input_path, memory_space):
        self.memory_space = memory_space
        self.corrupted = self.__get_data(input_path) 

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            return [tuple(map(int, line.strip().split(","))) for line in file]

    def __bfs(self, corrupted):
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        q = deque([(0,0)])
        visited = {(0,0)}
        reached_end = False 
        move_count = 0
        nodes_left_in_layer = 1
        nodes_in_next_layer = 0

        while q:
            r, c = q.popleft()

            if (r,c) == (self.memory_space, self.memory_space):
                reached_end = True
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited:
                    continue

                if nr < 0 or nc < 0:
                    continue

                if nr > self.memory_space or nc > self.memory_space:
                    continue

                if (nr, nc) in corrupted:
                    continue

                q.append((nr, nc))
                visited.add((nr, nc))
                nodes_in_next_layer += 1

            nodes_left_in_layer -= 1 
            if nodes_left_in_layer == 0:
                nodes_left_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                move_count += 1

        if reached_end:
            return move_count
        return -1

    def part_1(self, kb):
        corrupted = set(self.corrupted[:kb])
        steps = self.__bfs(corrupted)
        return steps

    def part_2(self):
        l, r = 0, len(self.corrupted)

        max_counter = 100
        i = 0
        while l < r and i < max_counter:
            i += 1
            corrupted = self.corrupted[:r]
            steps = self.__bfs(set(corrupted))

            if steps == -1:
                r = l + (r - l)//2
            else:
                l = r
                r += r//2

        return self.corrupted[r]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Syntax:")
        print("    python main.py <file.txt> <grid_size> <kb>")
        exit()

    input_file = sys.argv[1]
    memory_space = int(sys.argv[2])
    kb = int(sys.argv[3])
    advent = Advent(input_file, memory_space)
    part_1 = advent.part_1(kb)
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)

