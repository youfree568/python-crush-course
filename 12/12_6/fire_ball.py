import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, sl_game):

		super().__init__()
		self.screen = sl_game.screen
		self.settings = sl_game.settings
		self.color = self.settings.bullet_color

		# create bullet
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midright = sl_game.runner.rect.midright

	def update(self):
		self.rect.x -= 1

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)