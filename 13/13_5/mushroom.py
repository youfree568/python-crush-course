import pygame

from random import randint
from pygame.sprite import Sprite

class Mushroom(Sprite):

	def __init__(self, sl_game):
		"""fleet of mushrooms"""
		super().__init__()
		self.screen = sl_game.screen
		self.settings = sl_game.settings

		# load image of mushrooms
		self.image = pygame.image.load('image/mushroom.png')
		self.rect = self.image.get_rect()


		self.rect.left = self.screen.get_rect().right
		mushrom_top_max = self.settings.screen_height - self.rect.height
		self.rect.top = randint(0, mushrom_top_max)
		# start 
		# self.rect.x = self.settings.screen_width - (self.rect.width)
		# self.rect.y = self.rect.height

		# Store the mushrooms vertical position
		self.x = float(self.rect.x)


	def update(self):
		self.x -= self.settings.mushroom_speed
		self.rect.x = self.x