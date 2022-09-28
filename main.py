import pygame
import sys
from player_input import PlayerInput
from screen import Screen
from color import Color
from map import Map
from chip import Chip

width = 7
height = 6





def run_game():

	# Setup for the main game

	pygame.init()

	player_input = PlayerInput()
	map = Map(width, height)
	screen = Screen(width, height, map)

	chip = Chip(map, Color.red)

	game_over = False


	# Main game loop

	while game_over == False:
		player_input.get_input()

		if player_input.right == True and chip.x < width - 1:
			chip.x += 1
		if player_input.left == True and chip.x > 0:
			chip.x -= 1

		map.drop_chip(player_input, chip)

		map.detect_if_there_is_a_winner()

		game_over = map.win

		screen.update_screen(map, chip)


	# Setup for the win screen

	font = pygame.font.Font(None, 100)

	if map.winner == Color.red:
		text = "Red Wins"
	elif map.winner == Color.yellow:
		text = "Yellow Wins"

	text = font.render(text, True, map.winner)
	print(text.get_rect())


	# Win screen loop

	while 1 == 1:
		screen.draw_end_screen(map, text)
		player_input.get_input()

	pygame.quit()



if __name__ == "__main__":
	run_game()