import pygame

# from alien_invasion import ai_game

class Ship:
	"""ship control"""

	def __init__(self, ai_game):
		"""ship initialization and set position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# load image of the ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship in the center, bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""draw the ship in it's current location"""
		self.screen.blit(self.image, self.rect)