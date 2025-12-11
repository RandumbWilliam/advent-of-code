from collections import deque


class Advent:
    def __init__(self, input_path):
        self.garden = {}
        self.__get_data(input_path)

    def __get_data(self, input_path):
        with open(input_path, "r") as file:
            lines = [list(line.strip()) for line in file]

        for i, row in enumerate(lines):
            for j, value in enumerate(row):
                loc = i + j * 1j
                self.garden[loc] = value

    def __get_perimeter(self, plot):
        perimeter = 0

        directions = [-1, 1j, 1, -1j]

        for plant_loc in plot:
            for d in directions:
                loc_prime = plant_loc + d
                if loc_prime not in plot:
                    perimeter += 1

        return perimeter

    def __get_sides(self, plot):
        corners = 0

        for plant_loc in plot:
            # outer top-left
            if (plant_loc - 1) not in plot and (plant_loc - 1j) not in plot:
                corners += 1
            # outer top-right
            if (plant_loc - 1) not in plot and (plant_loc + 1j) not in plot:
                corners += 1
            # outer bottom-left
            if (plant_loc + 1) not in plot and (plant_loc - 1j) not in plot:
                corners += 1
            # outer bottom-right
            if (plant_loc + 1) not in plot and (plant_loc + 1j) not in plot:
                corners += 1

            # inner top-left
            if (
                (plant_loc + 1) in plot
                and (plant_loc + 1j) in plot
                and (plant_loc + (1 + 1j)) not in plot
            ):
                corners += 1
            # inner top-right
            if (
                (plant_loc) + 1 in plot
                and (plant_loc - 1j) in plot
                and (plant_loc + (1 - 1j)) not in plot
            ):
                corners += 1
            # inner bottom-left
            if (
                (plant_loc - 1) in plot
                and (plant_loc + 1j) in plot
                and (plant_loc + (-1 + 1j)) not in plot
            ):
                corners += 1
            # inner bottom-right
            if (
                (plant_loc - 1) in plot
                and (plant_loc - 1j) in plot
                and (plant_loc + (-1 - 1j)) not in plot
            ):
                corners += 1

        return corners

    def __bfs(self, plant, start_loc, visited):
        plot = set()
        directions = [-1, 1j, 1, -1j]

        q = deque([start_loc])
        visited.add(start_loc)
        plot.add(start_loc)

        while q:
            loc = q.popleft()

            for d in directions:
                loc_prime = loc + d
                if loc_prime in self.garden and loc_prime not in visited:
                    if self.garden[loc_prime] == plant:
                        q.append(loc_prime)
                        visited.add(loc_prime)
                        plot.add(loc_prime)

        return plot, visited

    def part_1(self):
        visited = set()
        cost = 0
        for plant_loc in self.garden:
            if plant_loc not in visited:
                plot, new_visited = self.__bfs(
                    self.garden[plant_loc], plant_loc, visited
                )
                visited = new_visited
                perimeter = self.__get_perimeter(plot)
                cost += len(plot) * perimeter

        return cost

    def part_2(self):
        visited = set()
        cost = 0
        for plant_loc in self.garden:
            if plant_loc not in visited:
                plot, new_visited = self.__bfs(
                    self.garden[plant_loc], plant_loc, visited
                )
                visited = new_visited
                perimeter = self.__get_sides(plot)
                cost += len(plot) * perimeter

        return cost


if __name__ == "__main__":
    advent = Advent("input.txt")
    part_1 = advent.part_1()
    part_2 = advent.part_2()

    print(part_1)
    print(part_2)
