import sys
import pygame

from random import randint

from settings import Settings
from units import Unit

class Stars:

	def __init__(self):
		"""initialization"""
		pygame.init()
		self.settings = Settings()
		
		# fullscreen mode
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		
		self.units = pygame.sprite.Group()

		self._create_fleet()
		# small screen mode
		# self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))	
		# name on the screen
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):

		while True:
			
			self._check_events()
			
			# background color
			self.screen.fill(self.settings.bg_color)
			# draw star
			self.units.draw(self.screen)
			#  show last one drawing screen
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()

	def _create_fleet(self):

		unit = Unit(self)
		unit_width, unit_height = unit.rect.size
		available_space_x = self.settings.screen_width - (2 * unit_width)
		number_units_x = available_space_x // (2 * unit_width)

		available_space_y = self.settings.screen_height - (2 * unit_width)
		number_rows = available_space_y // (2 * unit_height)

		for row_number in range(number_rows):
			for unit_number in range(number_units_x):
				unit = Unit(self)
				unit_width, unit_height = unit.rect.size
				unit.x = unit_width + 2 * unit_width * unit_number + randint(-20, 20)
				unit.rect.x = unit.x
				
				unit.rect.y = unit.rect.height + 2 * unit.rect.height * row_number + randint(-20, 20)
				self.units.add(unit)

if __name__=='__main__':
	st = Stars()
	st.run_game()