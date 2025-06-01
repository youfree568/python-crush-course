import pygame
from pygame.sprite import Sprite

class Unit(Sprite):

	def __init__(self, stars):

		super().__init__()
		self.screen = stars.screen

		# Load image
		self.image = pygame.image.load('images/Untitled.bmp')
		self.rect = self.image.get_rect()

		# start each new star near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height