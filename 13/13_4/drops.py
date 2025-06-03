import pygame
from pygame.sprite import Sprite

class Drop(Sprite):

	def __init__(self, rain):

		super().__init__()
		self.screen = rain.screen
		self.settings = rain.settings

		# Load image
		self.image = pygame.image.load('images/raindrop.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_disappeared(self):
		if self.rect.top >= self.settings.screen_height:
			return True
		else:
			return False

	def update(self):

		self.y += (self.settings.rain_drop_speed)
		self.rect.y = self.y