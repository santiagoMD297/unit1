import random

class MiningGrid:

    def __init__(self):
        self.grid = []

    def generate_random(self, rows, cols, min_val, max_val):
        """Create a grid of random values"""
        self.grid = []  # reset grid
        for r in range(rows):
            new_row = []
            for c in range(cols):
                number = random.randint(min_val, max_val)
                new_row.append(number)
            self.grid.append(new_row)
        return self.grid

    def mine_sector(self, location, amount):
        """Mine minerals from one spot"""
        x = location[0]
        y = location[1]
        current = self.grid[x][y]

        if amount >= current:
            mined = current
            self.grid[x][y] = 0
        else:
            mined = amount
            self.grid[x][y] = current - amount

        return mined

    def bulk_mine(self, mine_list):
        """Mine multiple places"""
        total = 0
        for mine in mine_list:
            x = mine[0]
            y = mine[1]
            amount = mine[2]
            mined_here = self.mine_sector((x, y), amount)
            total += mined_here
        return total

    def find_richest_sector(self):
        """Find the biggest number in the grid"""
        richest = 0
        richest_spot = (0, 0)

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] > richest:
                    richest = self.grid[r][c]
                    richest_spot = (r, c, richest)

        return richest_spot

    def find_depleted_sectors(self):
        """Find all (x,y) spots that are 0"""
        empty_spots = []

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 0:
                    empty_spots.append((r, c))

        return empty_spots

    def average_resource_level(self):
        """Average value of all minerals"""
        total = 0
        count = 0

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                total += self.grid[r][c]
                count += 1

        if count == 0:
            return 0
        else:
            return total / count


# TEST RUN
mine = MiningGrid()
print(mine.generate_random(5, 5, 10, 100))
print("Richest spot:", mine.find_richest_sector())
print("Average:", mine.average_resource_level())