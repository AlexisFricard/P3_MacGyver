import pygame
from game.constants import TILE_SIZE
import game.loads as loads
import time

def draw(level, macgyver, images, window):

	line_nb = 0
	for line in level.maze_map:
		case_nb = 0
		for sprite in line:
			pixel_position = (case_nb * TILE_SIZE ,line_nb * TILE_SIZE)
			if sprite == 'W' : 
				window.blit(images.wall(), pixel_position)
			elif sprite == '@' and macgyver.conjoncture != "WIN" :
				window.blit(images.guardian(), pixel_position)
			elif sprite == 'A' :
				window.blit(images.side_wall(), pixel_position)
			elif sprite == 'D' :
				window.blit(images.door(), pixel_position)
			elif sprite == 'Y':
				window.blit(images.flag_items(), pixel_position)
			elif sprite == 'Z':
				if macgyver.nb_items == 0:
					window.blit(images.nb_item0(), pixel_position)
				if macgyver.nb_items == 1:
					window.blit(images.nb_item1(), pixel_position)
				if macgyver.nb_items == 2:
					window.blit(images.nb_item2(), pixel_position)
				if macgyver.nb_items == 3:
					window.blit(images.nb_item3(), pixel_position)
			else:
				window.blit(images.floor(), pixel_position)

			case_nb += 1
		line_nb += 1	

	for item in level.items:
		if level.items[item].visible:
			window.blit(images.items[item](), level.items[item].sprite_position)

	if macgyver.conjoncture == "IN_PROGRESS":
		window.blit(images.macgyver(), macgyver.sprite_position)

	elif macgyver.conjoncture == "LOST":
		window.blit(images.loose_flag(), (0,0))

	elif macgyver.conjoncture == "WIN":
		window.blit(images.win_flag(), (0,0))

	pygame.display.flip()
#elif macgyver.conjoncture == "LOST":