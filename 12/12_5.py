import pygame
import sys

class CheckKeyDown:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Check Button")

	def run(self):
		while True:
			# self.screen.fill()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					print(event.key)
			pygame.display.flip()
if __name__=='__main__':
	CheckKeyDown().run()