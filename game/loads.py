"""
Loading Module - Json file, images ,generate the maze
"""

import json
import pygame

class Images:
    """ Load each image of the json file parameter for use in pygame """
    def __init__(self, setting):
		# Loading by class method the command to load an image
        self.pictures = {}
        for picture in setting["pictures"]:
            self.pictures[picture] = self.load_images(setting["pictures"][picture])
        self.items = {}
        for item in setting["items"]:
            self.items[item] = self.load_images(setting["items"][item])

    @classmethod
    def load_images(cls, image_link):
        """ Return the transparent pygame image load command """
        return pygame.image.load(image_link).convert_alpha


def initialize_maze_map(level_choice):
    """ Generate the file according to the chosen level """
    with open(level_choice, "r") as level_map:
        maze_map = [list(line) for line in level_map]
    return maze_map


def setting_from_file(file_name):
    """ Load setting from given filename """
    with open(file_name) as sett:
        return json.load(sett)
