from random import randint
import game.item
from game.constants import TILE_WIDTH, TILE_HEIGHT

class Level:

	def __init__(self, maze_map, items):
		# load maze to modify it top put object/item
		self.maze_map = maze_map
		self.items = {}
		# for each args (here : item1 and item2) in items list
		for item in items:
			# create an object who have a list of random position
			self.items[item] = game.item.Item(self.random_item_position())

	def random_item_position(self):
		pos_x = 0
		pos_y = 0
		while self.maze_map[pos_y][pos_x] != " ":
			pos_x = randint(0, TILE_WIDTH - 1 )
			pos_y = randint(0, TILE_HEIGHT - 1)
		self.maze_map[pos_y][pos_x] = "-"
		return (pos_x, pos_y)

	def autorized_path(self, pos_x, pos_y, direction):
		#if direction is not a wall, a ang_wall, and the limit of window
		# A REVOIR CAR PAS TOUT COMPRIS
		if direction == 'RIGHT' and pos_x < (TILE_WIDTH - 1) and self.maze_map[pos_y][pos_x + 1] != "W" and self.maze_map[pos_y][pos_x + 1] != "A":
			return True
		elif direction == 'LEFT' and pos_x > 0 and self.maze_map[pos_y][pos_x - 1] != "W" and self.maze_map[pos_y][pos_x - 1] != "A":
			return True
		elif direction == 'UP' and pos_y > 0 and self.maze_map[pos_y - 1][pos_x] != "W" and self.maze_map[pos_y - 1][pos_x] != "A":
			return True
		elif direction == 'DOWN' and pos_y < (TILE_HEIGHT - 1) and self.maze_map[pos_y + 1][pos_x] != "W" and self.maze_map[pos_y + 1][pos_x] != "A":
			return True