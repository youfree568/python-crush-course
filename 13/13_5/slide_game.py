import pygame
import sys

from settings import Settings
from runner import Runner
from fire_ball import Bullet
from mushroom import Mushroom

class SlideGame:

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height))
		pygame.display.set_caption("Slide Game")
		self.runner = Runner(self)
		self.bullets = pygame.sprite.Group()
		self.mushrooms = pygame.sprite.Group()

		self._create_fleet()


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
		self._update_bullets()
		self.mushrooms.draw(self.screen)

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
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
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
			

	def _update_bullets(self):
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

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

	# def _create_fleet(self):
	# 	"""create fleet of mushrooms"""
	# 	mushroom = Mushroom(self)
	# 	mushroom_width = mushroom.rect.width
	# 	available_space_x = self.settings.screen_width - (2 * mushroom_width)
	# 	number_mushroom_x = available_space_x // (2 * mushroom_width)

	# 	# create first row
	# 	for mushroom_number in range(number_mushroom_x):
	# 		# create mushroom and add him to row
	# 		mushroom = Mushroom(self)
	# 		mushroom.x = mushroom_width + 2 * mushroom_width * mushroom_number
	# 		mushroom.rect.x = mushroom.x
	# 		self.mushrooms.add(mushroom)

	def _create_fleet(self):
			"""create fleet of mushrooms"""
			mushroom = Mushroom(self)
			mushroom_height = mushroom.rect.height
			available_space_y = (self.settings.screen_height - (2 * mushroom_height))
			number_mushroom_y = available_space_y // (2 * mushroom_height)

			# create first row
			for mushroom_number in range(number_mushroom_y):
				# create mushroom and add him to row
				mushroom = Mushroom(self)
				mushroom.y = mushroom_height + 2 * mushroom_height * mushroom_number
				mushroom.rect.y = mushroom.y
				self.mushrooms.add(mushroom)


if __name__=='__main__':
	sd = SlideGame()
	sd.run()
