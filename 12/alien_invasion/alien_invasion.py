import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""Main class that manages game resources and behavior"""

	def __init__(self):
		"""Game initialization, create resources of game"""
		pygame.init()
		self.settings = Settings()		
		# fullscreen mode
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# window screen mode
		# self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		

	def run_game(self):
		"""Start the main game cycle"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()

	def _update_screen(self):	
		# redraw the screen on each iteration of the loop
		self.screen.fill(self.settings.bg_color)
		# show last screen
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		pygame.display.flip()

			
	def _check_events(self):
		# monitor mouse and keyboard events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		# check and move if key press down
		if event.key == pygame.K_RIGHT:
			# move ship right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# move ship left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			# when press 'q' quit from game
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		# check and stop moving if key up
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""create new bullet and add to bullet group"""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""update bullet position and delete old bullet"""
		# update bullet position
		self.bullets.update()
		# delete bullet under screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		# check if bullet hit alien
		# if bullet hit alien remove alien and bullet
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if not self.aliens:
			# removo all bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()

	def _create_fleet(self):
		"""create alien fleet"""
		# create aliens and find count aliens in row
		# space between aliens equel width one alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# find out how many lines will be on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
							(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# create first row of aliens
		for row_numbers in range(number_rows):	
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_numbers)
	
	def _create_alien(self, alien_number, row_numbers):
			alien = Alien(self)
			alien_width, alien_height = alien.rect.size
			alien.x = alien_width + 2 * alien_width * alien_number
			alien.rect.x = alien.x
			alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_numbers
			self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""reaction if alien touch end of the screen"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""move fleet down and change direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
	
	def _update_aliens(self):
		"""update aliens position"""
		self._check_fleet_edges()
		self.aliens.update()

	


if __name__=='__main__':
	# create a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()