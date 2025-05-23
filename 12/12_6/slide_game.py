import pygame
import sys

from settings import Settings
from runner import Runner
from fire_ball import Bullet

class SlideGame:

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height))
		pygame.display.set_caption("Slide Game")
		self.runner = Runner(self)
		self.bullets = pygame.sprite.Group()

	def run(self):

		while True:
			self._check_events()
			self.runner.move()
			self._update_fire_ball()
			self._update_screen()
			
	def _update_screen(self):
		self.screen.fill((self.settings.bg_color))
		self.runner.blitme()
			# bullet shot
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# check if button press
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				# check if button unpress
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		# check if button press
		if event.key == pygame.K_UP:
			self.runner.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.runner.moving_down = True
		elif event.key == pygame.K_SPACE:
			# make a shot
			self._fire_bullet()
				
	def _check_keyup_events(self, event):			
		# check if button unpress
		if event.key == pygame.K_UP:
			self.runner.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.runner.moving_down = False
			
	def _fire_bullet(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_fire_ball(self):
		# update bullet position and delete old bullet
		# update bullet position
		self.bullets.update()
		# delete bullet under screen
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen.get_rect().right:
				# print(len(self.bullets))
				self.bullets.remove(bullet)

if __name__=='__main__':
	sd = SlideGame()
	sd.run()