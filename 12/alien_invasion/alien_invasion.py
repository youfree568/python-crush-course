import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Main class that manages game resources and behavior"""

	def __init__(self):
		"""Game initialization, create resources of game"""
		pygame.init()
		self.settings = Settings()		
	
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main game cycle"""
		while True:
			self._check_events()
			self._update_screen()
			
	def _update_screen(self):	
		# redraw the screen on each iteration of the loop
		self.screen.fill(self.settings.bg_color)
		# show last screen
		self.ship.blitme()
		pygame.display.flip()
			
	def _check_events(self):
		# monitor mouse and keyboard events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

if __name__=='__main__':
	# create a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()