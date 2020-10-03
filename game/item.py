"""
Item's Module - To create an object
"""

from game.constants import TILE_SIZE

class Item:
    """ Creat an item with position """
    def __init__ (self, position):
        # pos_x = first attribute of list, etc..
        self.pos_x  = position[0]
        self.pos_y  = position[1]
        # to show or delete item if macgyver have allready it
        self.visible = True

    @property
    def sprite_position(self):
        """ Gives position's dimensions of the sprite """
        return (self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE)
