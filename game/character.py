from game.constants import TILE_SIZE

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