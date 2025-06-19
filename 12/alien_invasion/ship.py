import pygame

# from alien_invasion import ai_game

class Ship:
	"""ship control"""

	def __init__(self, ai_game):
		"""ship initialization and set position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# load image of the ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Create each new ship in the center, bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# store a decimal value for the ship's horizontal position 
		self.x = float(self.rect.x)
		# moving indicators
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update current position """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		# update object rect
		self.rect.x = self.x

	def blitme(self):
		"""draw the ship in it's current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""move ship to the center"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)