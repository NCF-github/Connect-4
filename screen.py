import pygame
from color import Color

class Screen:
	def __init__(self, map_width, map_height, map, BG_color = Color.light_gray, clock_tick = 60):
		self.width = map_width * map.cell_size
		self.height = (map_height + 1) * map.cell_size
		self.cell_size = map.cell_size

		self.BG_color = BG_color
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()
		self.clock_tick = clock_tick

	def update_screen(self, map, chip):
		self.screen.fill(self.BG_color)
		map.draw(self.screen)
		chip.draw(self.screen)

		pygame.display.update()
		self.clock.tick(self.clock_tick)

	def draw_end_screen(self, map, text):
		self.screen.fill(self.BG_color)
		map.draw(self.screen)
		text_rect = text.get_rect()
		self.screen.blit(text, (self.width / 2 - text_rect[2] / 2, self.cell_size / 2 - text_rect[3] / 2))

		pygame.display.update()
		self.clock.tick(self.clock_tick)
