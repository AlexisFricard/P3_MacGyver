import pygame
from pygame.locals import *
from constantes import *


############ LEVEL ############

class Level:

	def __init__(self, level_file_name):
		self.level_file_name = level_file_name
		self.structure = 0

	### MAZE_MAP ###

	# This is how generate maze map in function of the name file ("L1", "L2")
	def generate_maze_map(self):
		# Open the file 
		with open(self.level_file_name, "r") as level_file_name:
			# List which contains lists of each ligne
			level_structure = []
			# for each line in file 
			for line in level_file_name:
				# list of each line
				level_line = []
				# for each character in this line
				for sprite in line:
					# Forget the /n
					if sprite != "\n":
						# Add sprite in this list ligne
						level_line.append(sprite)
				#  Add this list ligne in the list of level structure
				level_structure.append(level_line)
			# Save this structure level
			self.structure = level_structure

	# This is how assossiated image to sprite to show maze_map
	def show_maze_map(self, window):

		wall = pygame.image.load("Images/wall.png").convert_alpha()
		floor = pygame.image.load("Images/floor.png").convert_alpha()
		door = pygame.image.load("Images/door.png").convert_alpha()
		ang_wall = pygame.image.load("Images/Ang_wall.png").convert_alpha()
		guardian = pygame.image.load("Images/guardian.png").convert_alpha()

		line_nb = 0
		for line in self.structure:
			case_nb = 0
			for sprite in line:
				x = case_nb * TILE_SIZE
				y = line_nb * TILE_SIZE
				if sprite == 'W' : 
					window.blit(wall, (x,y))
				elif sprite == '@' :
					window.blit(guardian, (x,y))
				elif sprite == 'A' :
					window.blit(ang_wall, (x,y))
				elif sprite == '0' :
					window.blit(floor, (x,y))
				elif sprite == 'D' :
					window.blit(door, (x,y))						
				case_nb += 1
			line_nb += 1
		pygame.display.flip()

############ MACGYVER ############
class MacGyver:

	def __init__(self, Mac_Gyver, level):
		# Initialize image of MacGyver
		self.Mac_Gyver = pygame.image.load(Mac_Gyver).convert_alpha()
		# add level_choice in attribut
		self.level = level
		#Inital position
		self.case_x = 1 # in cases
		self.case_y = 1
		self.x = self.case_x * TILE_SIZE		# in pixels
		self.y = self.case_y * TILE_SIZE

		self.direction = self.Mac_Gyver
		# the first case (0,0) is in the top corner left

	### METHODE TO MOOVE IN MAZE MAP ###
	def moove_to(self, direction):

		if direction == 'right':
			# To not go out the screen
			# If my position is inf to my tile width -1 = (15)-1 = (0 to 14) 15cases 
			if self.case_x < (TILE_WIDTH -1):
				#We check if is not a wall
				if self.level.structure[self.case_y][self.case_x + 1] != 'W' and self.level.structure[self.case_y][self.case_x + 1] != 'A':
					self.case_x += 1
					self.x = self.case_x * TILE_SIZE
			self.direction = self.Mac_Gyver
		if direction == 'left':
			# To not go out the screen
			# If my position is strictly sup to my first case of width (0)
			if self.case_x > 0:
				#We check if is not a wall
				if self.level.structure[self.case_y][self.case_x -1] != 'W' and self.level.structure[self.case_y][self.case_x -1] != 'A':
					self.case_x -= 1
					self.x = self.case_x * TILE_SIZE
		if direction == 'up':
			# To not go out the screen
			# If my position is strictly sup to my first case of height (0)
			if self.case_y > 0:
				#We check if is not a wall
				if self.level.structure[self.case_y - 1][self.case_x] != 'W' and self.level.structure[self.case_y - 1][self.case_x] != 'A':
					self.case_y -= 1
					self.y = self.case_y * TILE_SIZE
		if direction == 'down':
			# To not go out the screen
			# If my position is inf to my tile height -1 = (15)-1 = (0 to 14) 15cases 
			if self.case_y < (TILE_HEIGHT - 1):
				#We check if is not a wall
				if self.level.structure[self.case_y + 1][self.case_x] != 'W' and self.level.structure[self.case_y + 1][self.case_x] != 'A':
					self.case_y += 1
					self.y = self.case_y * TILE_SIZE


