import pygame
import sys

from settings import Settings

class Rocket:

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("ROCKET")
		# initialization rocket
		self.image = pygame.image.load('rocket.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center

		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

	def run_game(self):
		while True:			
			self.move_rocket()
			# draw background
			self.screen.fill(self.settings.bg_color)
			# draw rockt
			self.screen.blit(self.image, self.rect)
			# show screen last time
			pygame.display.flip()
			self._move()
			
	def move_rocket(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_key_down(event)
			elif event.type == pygame.KEYUP:
				self._check_key_up(event)

	def _check_key_down(self, event):
		if event.key == pygame.K_RIGHT:
			self.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.moving_left = True
		elif event.key == pygame.K_DOWN:
			self.moving_down = True
		elif event.key == pygame.K_UP:
			self.moving_up = True
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_key_up(self, event):
		if event.key == pygame.K_RIGHT:
			self.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.moving_left = False
		elif event.key == pygame.K_DOWN:
			self.moving_down = False
		elif event.key == pygame.K_UP:
			self.moving_up = False

	def _move(self):
		if self.moving_left and self.rect.left > 0:
			self.rect.x -= 1
		elif self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += 1
		elif self.moving_up and self.rect.top > 0:
			self.rect.y -= 1
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 1


if __name__=='__main__':
	Rocket().run_game()
