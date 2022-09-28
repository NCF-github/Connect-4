import pygame
from color import Color
from chip import Chip

class Map():
	def __init__(self, map_width, map_height, cell_size = 100, color = Color.blue):
		self.cell_size = cell_size
		self.rect = (0, self.cell_size, map_width * self.cell_size, map_height * self.cell_size)
		self.color = color

		self.map = [[Chip(self, Color.light_gray, x, y + 1) for x in range(map_width)] for y in range(map_height)]

		self.win = False
		self.winner = None

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
		for row in self.map:
			for chip in row:
				chip.draw(screen)

	def drop_chip(self, player_input, chip):
		a = 0
		if player_input.space == True:
			for row in self.map:
				if row[chip.x].color == Color.light_gray:
					a += 1
		if a != 0:
			self.map[a - 1][chip.x].color = chip.color
			if chip.color == Color.red:
				chip.color = Color.yellow
			elif chip.color == Color.yellow:
				chip.color = Color.red

	def detect_win_vertical(self):
		for y in range(len(self.map) - 3):
			for x in range(len(self.map[y])):
				count = 0
				if self.map[y][x].color != Color.light_gray:
					for i in range(4):
						if self.map[y + i][x].color == self.map[y][x].color:
							count += 1
					if count == 4:
						self.win = True
						self.winner = self.map[y][x].color
						for i in range(4):
							if self.map[y + i][x].size == 40:
								self.map[y + i][x].size = 45

	def detect_win_horizontal(self):
		for row in self.map:
			for x in range(len(row) - 3):
				count = 0
				if row[x].color != Color.light_gray:
					for i in range(4):
						if row[x + i].color == row[x].color:
							count += 1
					if count == 4:
						self.win = True
						self.winner = row[x].color
						for i in range(4):
							if row[x + i].size == 40:
								row[x + i].size = 45

	def detect_win_diagonal_up_right(self):
		for y in range(len(self.map) - 3):
			for x in range(len(self.map[y]) - 3):
				count = 0
				if self.map[y + 3][x].color != Color.light_gray:
					for i in range(4):
						if self.map[y + 3 - i][x + i].color == self.map[y + 3][x].color:
							count += 1
					if count == 4:
						self.win = True
						self.winner = self.map[y + 3][x].color
						print("Win")
						for i in range(4):
							if self.map[y + 3 - i][x + i].size == 40:
								self.map[y + 3 - i][x + i].size = 45

	def detect_win_diagonal_down_right(self):
		for y in range(len(self.map) - 3):
			for x in range(len(self.map[y]) - 3):
				count = 0
				if self.map[y][x].color != Color.light_gray:
					for i in range(4):
						if self.map[y + i][x + i].color == self.map[y][x].color:
							count += 1
					if count == 4:
						self.win = True
						self.winner = self.map[y][x].color
						for i in range(4):
							if self.map[y + i][x + i].size == 40:
								self.map[y + i][x + i].size = 45

	def detect_if_there_is_a_winner(self):
		self.detect_win_vertical()
		self.detect_win_horizontal()
		self.detect_win_diagonal_up_right()
		self.detect_win_diagonal_down_right()
