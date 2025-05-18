import sys
import pygame

class BlueSky:

	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Blue Sky")

	def run(self):

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.screen.fill((0, 0, 230))
			pygame.display.flip()

if __name__=='__main__':
	BlueSky().run()