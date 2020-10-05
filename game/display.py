"""
Drawing Module - Draw what should happen on the screen !
"""

import pygame
from game.constants import TILE_SIZE

def draw(level, macgyver, images, window):
    """ Method to draw each case """
    if macgyver.conjoncture == "IN_PROGRESS":
        line_nb = 0
        for line in level.maze_map:
            case_nb = 0
            for sprite in line:

                pixel_position = (case_nb * TILE_SIZE ,line_nb * TILE_SIZE)
                typ_of_char = { "W": "wall", "@": "guardian", "A": "side_wall",
                                "D": "door", "Y": "flag_items"}

                if sprite in ("W", "@", "A", "D", "Y"):
                    if sprite == "@":
                        window.blit(images.pictures["floor"](), pixel_position)
                    typ_of_let = typ_of_char[sprite]
                    window.blit(images.pictures[typ_of_let](), pixel_position)

                elif sprite == 'Z':
                    for item in range(0, macgyver.nb_items + 1):
                        window.blit(images.pictures["nb_item{}".format(item)](), pixel_position)
                else:
                    window.blit(images.pictures["floor"](), pixel_position)


                case_nb += 1
            line_nb += 1
        window.blit(images.pictures["macgyver"](), macgyver.sprite_position)

    for item in level.items:
        if level.items[item].visible:
            window.blit(images.items[item](), level.items[item].sprite_position)

    if macgyver.conjoncture == "LOST":
        window.blit(images.pictures["loose_flag"](), (0,0))

    elif macgyver.conjoncture == "WIN":
        window.blit(images.pictures["win_flag"](), (0,0))

    pygame.display.flip()
