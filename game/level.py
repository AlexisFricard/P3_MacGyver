"""
Level module - Initializes the items and to a function if the path is free
"""

from random import randint
import game.item as itm
from game.constants import TILE_WIDTH, TILE_HEIGHT

class Level:
    """ Get item and is position, and if character are autorized to pass """
    def __init__(self, maze_map, items):
        self.maze_map = maze_map
        self.items = {}
        for item in items:
            self.items[item] = itm.Item(self.random_item_position())

    def random_item_position(self):
        """ Give a random position to the item """
        pos_x = 0
        pos_y = 0
        while self.maze_map[pos_y][pos_x] != " ":
            pos_x = randint(0, TILE_WIDTH - 1 )
            pos_y = randint(0, TILE_HEIGHT - 1)
        self.maze_map[pos_y][pos_x] = "-"
        return (pos_x, pos_y)

    def autorized_path(self, pos_x, pos_y, direction):
        """ Passage check """
        return (direction == 'RIGHT' and pos_x < (TILE_WIDTH - 1) and
        self.maze_map[pos_y][pos_x + 1] != "W" and
        self.maze_map[pos_y][pos_x + 1] != "A" or
        direction == 'LEFT' and pos_x > 0 and
        self.maze_map[pos_y][pos_x - 1] != "W" and
        self.maze_map[pos_y][pos_x - 1] != "A" or
        direction == 'UP' and pos_y > 0 and
        self.maze_map[pos_y - 1][pos_x] != "W" and
        self.maze_map[pos_y - 1][pos_x] != "A" or
        direction == 'DOWN' and pos_y < (TILE_HEIGHT - 1) and
        self.maze_map[pos_y + 1][pos_x] != "W" and
        self.maze_map[pos_y + 1][pos_x] != "A")
