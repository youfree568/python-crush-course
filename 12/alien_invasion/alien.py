import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self, ai_game):
		"""class that introduce alien fleet"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and its rect attribute.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

	def check_edges(self):
		"""return True if alien out of the screen"""	
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""move alien right or left"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x
