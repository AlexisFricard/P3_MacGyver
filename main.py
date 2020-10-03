# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
Jeu : Aidez Mac_Gyver à s'échapper !

Jeu dans lequel on dois déplacer Mac_Gyver à travers un labyrinthe,
ramasser trois objets et endormir le gardien de la porte.

Script Python

Fichiers:

setting.json, LVL1.xsb, LVL2.xsb, main.py, game/ [display.py, character.py, level.py, item.py,
constants.py], images/ [wall.png, floor.png, etc..]

"""

import time
import pygame
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE, K_F1, K_F2, K_RIGHT, K_LEFT, K_UP, K_DOWN

import game.loads as loads
import game.display as display
import game.level as set_funct
import game.character as character
from game.constants import WINDOW_WIDTH, WINDOW_HEIGHT


def main():
    """ Main code """

    setting = loads.setting_from_file('setting.json')
    images = loads.Images(setting)

    ### INITIALIZATION OF THE WINDOW ###
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_icon(images.pictures["icon"]())
    pygame.display.set_caption("Aidez MacGyver à s'échapper !!")

    ### MAIN LOOP ###
    still_continue = 1
    while still_continue:

        # Initialize variables selections
        menu_continue = 1
        game_continue = 1

        ### MENU LOOP ###
        while menu_continue:
            # Show menu
            window.blit(images.pictures["background_menu"](), (0,0))
            pygame.display.flip()
            # If user want to leave
            for event in pygame.event.get() :
                # if user leave, turn down all variables selections
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    menu_continue = 0
                    game_continue = 0
                    still_continue = 0
                    level_choice = ''
                #Selection of the maze
                elif event.type == KEYDOWN:
                    # If user event is F1 to first level
                    if event.key == K_F1:
                        # Selected level
                        level_choice = 'LVL1.xsb'
                        # To leave MENU LOOP
                        menu_continue = 0

                    elif event.key == K_F2:
                        level_choice = 'LVL2.xsb'
                        menu_continue = 0
                        ### MENU LOOP ###

        ### CHOICE CHECKING ###
        if level_choice != '' :
            # Initialize map from file level and add it with items in attribute
            level = set_funct.Level(loads.initialize_maze_map(level_choice), setting["items"])
            # Initalization of macgyver
            macgyver = character.Character(level, setting["items"])
            # Draw each objects
            display.draw(level, macgyver, images, window)

        ### GAME LOOP ###
        while game_continue:
            for event in pygame.event.get():
                # If user leave in game close window
                if event.type == QUIT:
                    game_continue = 0
                    still_continue = 0

                elif event.type == KEYDOWN:
                    # If user say ESCAPE, go back to menu loop
                    if event.key == K_ESCAPE:
                        game_continue = 0
                    # Deplacement of MacGyver
                    elif event.key == K_RIGHT:
                        macgyver.moove_to('RIGHT')
                    elif event.key == K_LEFT:
                        macgyver.moove_to('LEFT')
                    elif event.key == K_UP:
                        macgyver.moove_to('UP')
                    elif event.key == K_DOWN:
                        macgyver.moove_to('DOWN')

                # If macgyver loose or win the game wait 3 sec
                elif macgyver.conjoncture != "IN_PROGRESS":
                    time.sleep(3)
                    game_continue = 0

                # Draw each objects
                display.draw(level, macgyver, images, window)
                ### GAME LOOP ###
                ### MAIN LOOP ###

if __name__ == "__main__":
    main()
