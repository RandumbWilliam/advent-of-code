from collections import deque


class Advent:
    def __init__(self, input_path):
        self.topographic_map = {}
        self.start_locations = []
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(map(int, line.strip())) for line in file]

        for i, row in enumerate(lines):
            for j, value in enumerate(row):
                loc = i + j * 1j
                self.topographic_map[loc] = value
                if value == 0:
                    self.start_locations.append(loc)

    def __bfs(self, start_loc):
        trailhead = 0
        visited = set()
        directions = [-1, 1j, 1, -1j]

        q = deque([start_loc])
        visited.add(start_loc)

        while q:
            loc = q.popleft()
            if self.topographic_map[loc] == 9:
                trailhead += 1

            for d in directions:
                loc_prime = loc + d
                if loc_prime in self.topographic_map and loc_prime not in visited:
                    if self.topographic_map[loc_prime] == self.topographic_map[loc] + 1:
                        q.append(loc_prime)
                        visited.add(loc_prime)

        return trailhead

    def __ratings(self, start_loc):
        directions = [-1, 1j, 1, -1j]

        ratings = 0

        def dfs(loc, visited):
            nonlocal ratings

            if self.topographic_map[loc] == 9:
                ratings += 1
                return

            visited.add(loc)

            for d in directions:
                loc_prime = loc + d
                if loc_prime in self.topographic_map and loc_prime not in visited:
                    if self.topographic_map[loc_prime] == self.topographic_map[loc] + 1:
                        dfs(loc_prime, visited)

            visited.remove(loc)

        dfs(start_loc, set())

        return ratings

    def part_1(self):
        locs = self.start_locations
        trailhead_sum = 0
        for loc in locs:
            trailhead_sum += self.__bfs(loc)

        return trailhead_sum

    def part_2(self):
        locs = self.start_locations
        ratings_sum = 0
        for loc in locs:
            ratings_sum += self.__ratings(loc)

        return ratings_sum


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
