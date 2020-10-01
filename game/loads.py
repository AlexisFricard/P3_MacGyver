import pygame
import json
from pygame.locals import *

class Images:

	def __init__(self, setting):
		# Loading by class method the command to load in pygame an image
		self.wall = self.load_image(setting["wall"])
		self.side_wall = self.load_image(setting["side_wall"])
		self.floor = self.load_image(setting["floor"])
		self.background_menu = self.load_image(setting["background_menu"])
		self.door = self.load_image(setting["door"])
		self.guardian = self.load_image(setting["guardian"])
		self.loose_flag = self.load_image(setting["loose_flag"])
		self.win_flag = self.load_image(setting["win_flag"])
		self.macgyver = self.load_image(setting["macgyver"])
		self.icon = self.load_image(setting["icon"])
		self.flag_items = self.load_image(setting["flag_items"])
		self.nb_item0 = self.load_image(setting["nb_item0"])
		self.nb_item1 = self.load_image(setting["nb_item1"])
		self.nb_item2 = self.load_image(setting["nb_item2"])
		self.nb_item3 = self.load_image(setting["nb_item3"])			
		self.items = {}
		for item in setting["items"]:
			self.items[item] = self.load_image(setting["items"][item])


		#Here, items = ["pygame.image.load(images/item1.png).convert_alpha", ...]

	@classmethod
	def load_image(cls, image_link):
		return pygame.image.load(image_link).convert_alpha

### MAZE_MAP ###

def initialize_maze_map(level_choice):
		# Open the file 
		with open(level_choice, "r") as level_choice:
			# List which contains lists of each ligne
			maze_map = [list(line) for line in level_choice]
		return maze_map


def setting_from_file(file_name):
    """Load config from given filename"""
    with open(file_name) as data:
        return json.load(data)