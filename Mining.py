import random

class MiningGrid:

	def __init__(self):
		self.grid = []
  
	def generate_random(self, h, w, min_val, max_val):
		"""
		Generates a grid of size width (h * w) filled with random values
        between min_val and max_val
        """
		for row in range(h):
			row = []
			for num in range(w):
				number = random.randint(min_val, max_val)
				row.append(number)
			self.grid.append(row)


	def mine_sector(self, location:tuple, amount:int):
		"""
		Mines (removes) amount minerals at location. In the event not enough resources
        are present, they will all be mined and the sector would become 0 (depleted)

        Args:
        	location: an (x,y) tuple of the location
            amount: an int representing the amount of minerals to be extracted

        Returns:
        	int: the amount of minerals successfully mined

        
        """
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
		"""
		Mines the asteroid based on the locations and amount given in mine_list:

        Args:
        	mine_list (tuple): a list of tuples (x,y,a) containing the x, y location and the amount to be mined
            					ex: [ (3,4,100), (4, 9, 70) ]
        Returns:
        	the total amount mined from all locations
        """
		total = 0
		for mine in mine_list:
			total += self.grid.mine_sector(mine[0:1], mine[2])
		return total


	def find_richest_sector(self):
		g = self.grid
		richest = 0
		location = []

		for h in g:
			for w in h:
				if w > richest:
					richest = w
		hight = 0
		for h in g:
			width = 0
			for num in h:
				if num == richest:
					location.append(hight)
					location.append(width)
					return location
				width += 1
			hight += 1
				


		



	def find_depleted_sectors(self):
		"""
        Finds all sectors with 0 resources.
        Returns a list of (row, column) tuples.
        """
		locations0 = []
		g = self.grid
		h = 0
		for hight in g:
			w = 0
			for width in hight:
				if width == 0:
					
					



  	
	def average_resource_level(self):
		"""
        Calculates the average resource level of the asteroid.
        """
		pass

	def best_region(self):
		"""
      	Determines the best region (2x2 sectors) with the highest mineral count
        
        Returns:
        	A list of 4 (x, y) tuples
        """
		pass
mineg = MiningGrid()
print(mineg.generate_random(5,5,10,100))