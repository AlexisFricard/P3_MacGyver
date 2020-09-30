# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
Jeu : Aidez Mac_Gyver à s'échapper !
Jeu dans lequel on dois déplacer Mac_Gyver à travers un labyrinthe,
ramasser deux objets et endormir le gardien de la porte.

Script Python
Fichiers : 
"""
import time
import pygame
from pygame.locals import *

from game.constants import WINDOW_WIDTH, WINDOW_HEIGHT
import game.loads as loads
import game.functions as functions
import game.display as display


def main():
	#initialize pygame
	pygame.init()
	# Opened and custom the PyGame Window's
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))	# Open the window
	setting = loads.setting_from_file('setting.json') 				# setting = Dictionary :{"wall" = "images/wall.png",...}
	images = loads.Images(setting)  				  				# images = list of attributs wich contains images by link
	# Show icon
	pygame.display.set_icon(images.icon())
	# Show Title
	pygame.display.set_caption("Aidez MacGyver à s'échapper !!")

	### MAIN LOOP ###

	still_continue = 1

	while still_continue:
		# We show them
		window.blit(images.background_menu(), (0,0))
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
					menu_continue, game_continue, still_continue, level_choice = 0
				#Selection of the maze
				elif event.type == KEYDOWN:
	    			# If user tape F1 to first level
					if event.key == K_F1:
						menu_continue = 0	# To leave MENU LOOP
						level_choice = 'LVL1.xsb'	# Selected level
	    			# If user tape F2 for second level
					elif event.key == K_F2:
						menu_continue = 0
						level_choice = 'LVL2.xsb'

	    ### END OF MENU LOOP ###

	    #Check if user don't leave
		if level_choice != 0 :
			# Initialize map from file level
			# level = [[list_of [list ligne]], [link1 , link2]]
			level = functions.Level(loads.initialize_maze_map(level_choice), setting["items"])
			# level = [[[list_of [list level_file_ligne]], ["pygame.image.load(images/item1.png).convert_alpha", ...]]
	    	# Generate MacGyver with maze to add him (and know who he is) and list of item like precentlY
			macgyver = functions.Character(level, setting["items"]) # initalization de macgyver
			# Here, macgyver have attribute how much items he have, and his position 
			# Draw each objects
			display.draw(level, macgyver, images, window)

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

				elif macgyver.conjoncture != "IN_PROGRESS":
					time.sleep(3)
					game_continue = 0

				display.draw(level, macgyver, images, window)

if __name__ == "__main__":
	main()
