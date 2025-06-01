import sys
import pygame

from settings import Settings

class Stars:

	def __init__(self):
		"""initialization"""
		pygame.init()
		self.settings = Settings()
		
		# fullscreen mode
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		
		# small screen mode
		# self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))	
		# name on the screen
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()

			# background color
			self.screen.fill(self.settings.bg_color)
			#  show last one drawing screen
			pygame.display.flip()

if __name__=='__main__':
	st = Stars()
	st.run_game()