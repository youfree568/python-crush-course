import pygame

class Mario:

	def __init__(self, sl_game):

		self.screen = sl_game.screen
		self.settings = sl_game.settings
		self.screen_rect = sl_game.screen.get_rect()
		# load image
		self.image = pygame.image.load('image/retro_mario.png')
		self.rect = self.image.get_rect()
		# position 
		self.rect.midleft = self.screen_rect.midleft

		self.moving_up = False
		self.moving_down = False

	def move(self):
		# make mario move
		if self.moving_up == True and self.rect.top > 0:
			self.rect.y -= 1
		elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 1

	def blitme(self):
		# show mario on the screen
		self.screen.blit(self.image, self.rect)