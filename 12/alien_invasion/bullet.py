import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""class for bullet in our ship"""

	def __init__(self, ai_game):
		"""create bullet in current version of ship"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# create rect of bullet in (0, 0) and add current position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		"""move bullet up"""
		self.y -= self.settings.bullet_speed
		# update position
		self.rect.y = self.y

	def draw_bullet(self):
		"""draw bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
