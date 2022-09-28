import pygame
from color import Color

class Chip():
	def __init__(self, map, color, x = 0, y = 0, size = 40):
		self.size = size
		self.cell_size = map.cell_size
		self.x = x
		self.y = y
		self.color = color

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x * self.cell_size + self.cell_size / 2, self.y * self.cell_size + self.cell_size / 2), self.size)