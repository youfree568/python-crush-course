import pygame

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

		# start 
		self.rect.x = self.settings.screen_width - (self.rect.width)
		self.rect.y = self.rect.height

		# Store the mushrooms vertical position
		self.y = float(self.rect.y)