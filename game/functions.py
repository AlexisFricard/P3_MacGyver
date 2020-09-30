from random import randint
from game.constants import TILE_WIDTH, TILE_HEIGHT, TILE_SIZE

class Level:

	def __init__(self, maze_map, items):
		# load maze to modify it top put object/item
		self.maze_map = maze_map
		self.items = {}
		# for each args (here : item1 and item2) in items list
		for item in items:
			# create an object who have a list of random position
			self.items[item] = Item(self.random_item_position())

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

class Character:

	def __init__(self, level, items):
		self.level = level
		self.reset_position()

	def reset_position(self):
		self.pos_x, self.pos_y = self.initial_position(self.level)
		self.nb_items = 0

	def moove_to(self, direction):
		# If MacGyver can pass, increment or decrement its position by 1 case
		if self.level.autorized_path(self.pos_x, self.pos_y, direction):
			if direction == 'RIGHT':
				self.pos_x += 1
			elif direction == 'LEFT':
				self.pos_x -= 1
			elif direction == 'DOWN':
				self.pos_y += 1
			elif direction == 'UP':
				self.pos_y -= 1
		self.collect_items()

	def collect_items(self):
		# To longer to write for each item, perhead if we would like to add a new object
		for item in self.level.items:
			if (self.level.items[item].pos_x == self.pos_x and 
				self.level.items[item].pos_y == self.pos_y and 
				self.level.items[item].visible == True):
				self.nb_items += 1
				self.level.items[item].visible = False

	@classmethod
	def initial_position(cls, level):
        #Get initial character's position from the maze map
		num_line = 0
		for line in level.maze_map:
			num_column = 0
			for case in line:
				if case == "M":
					return (num_line, num_column)
				num_column += 1
			num_line += 1

	@property
	def sprite_position(self):
		return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]

	@property	
	def conjoncture(self):
		if self.level.maze_map[self.pos_y][self.pos_x] == '*':
			if self.nb_items == len(self.level.items):
				return "WIN"
			return "LOST"
		return "IN_PROGRESS"

class Item:
	#Création d'un objet item
	def __init__ (self, position):
		# pos_x = first attribute of list, etc..
		self.pos_x  = position[0]
		self.pos_y  = position[1]
		# to show or delete item if macgyver have allready it
		self.visible = True

	@property
	def sprite_position(self):
		return (self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE)