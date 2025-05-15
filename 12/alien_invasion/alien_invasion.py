import sys

import pygame

class AlienInvasion:
	"""Main class that manages game resources and behavior"""

	def __init__(self):
		"""Game initialization, create resources of game"""

		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Alien Invasion")
		# make background color
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Start the main game cycle"""
		while True:
			# monitor mouse and keyboard events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# redraw the screen on each iteration of the loop
			self.screen.fill(self.bg_color)
			# show last screen
			pygame.display.flip()

if __name__=='__main__':
	# create a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()