import pygame
import sys

class PlayerInput():
	def __init__(self):
		self.right = False
		self.left = False
		self.space = False

	def get_input(self):
		self.right = False
		self.left = False
		self.space = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.right = True
				if event.key == pygame.K_LEFT:
					self.left = True
				if event.key == pygame.K_SPACE:
					self.space = True

		if self.right == True and self.left == True:
			self.right, self.left == False, False