# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
Jeu : Aidez Mac_Gyver à s'échapper !
Jeu dans lequel on dois déplacer Mac_Gyver à travers un labyrinthe,
ramasser deux objets et endormir le gardien de la porte.

Script Python
Fichiers : 
"""
import pygame
from pygame.locals import *
from constantes import *
from loads import *
import time

#initialize pygame
pygame.init()
# Opened and custom the PyGame Window's
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Charge icone
icon = pygame.image.load(image_icon).convert_alpha()
pygame.display.set_icon(icon)
# Charge Title
pygame.display.set_caption(WINDOW_TITLE)

### MAIN LOOP ###

still_continue = 1
while still_continue:
	# MENU
	menu = pygame.image.load(background_menu).convert()

	# We show them
	window.blit(menu, (0,0))
	# refresh
	pygame.display.flip()

	# Initialize variables selections
	menu_continue = 1
	game_continue = 1

	### MENU LOOP ###

	while menu_continue:

		# If user want to leave
		for event in pygame.event.get() :
			# if user leave, turn down all variables selections
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				menu_continue = 0
				game_continue = 0
				still_continue = 0
				level_choice = 0

			#Selection of the maze
			elif event.type == KEYDOWN:
    			# If user tape F1 to first level
				if event.key == K_F1:
					menu_continue = 0	# To leave MENU LOOP
					level_choice = 'LVL1'	# Selected level
    			# If user tape F2 for second level
				elif event.key == K_F2:
					menu_continue = 0
					level_choice = 'LVL2'

    ### END OF MENU LOOP ###

    #Check if user don't leave
	if level_choice != 0 :
    	# Init File level
		level = Level(level_choice)
    	# Generate maze from file level
		level.generate_maze_map()
    	# Initialize maze map in window
		level.show_maze_map(window)


    	# Generate MacGyver
		mac_gyver = MacGyver(Mac_Gyver, level)

	while game_continue:
		pygame.time.Clock().tick(30)

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
					mac_gyver.moove_to('right')
				elif event.key == K_LEFT:
					mac_gyver.moove_to('left')
				elif event.key == K_UP:
					mac_gyver.moove_to('up')
				elif event.key == K_DOWN:
					mac_gyver.moove_to('down')  

#En l'endroit où il était il faut retamponner l'image de fond
# ajouter une méthode draw macgyver

			level.show_maze_map(window)				
			window.blit(mac_gyver.direction, (mac_gyver.x, mac_gyver.y))
			pygame.display.flip()

		if level.structure[mac_gyver.case_y][mac_gyver.case_x] == '@':
			win = pygame.image.load(win_flag).convert()
			window.blit(win, (0,0))
			pygame.display.flip()
			time.sleep(3)
			game_continue = 0
