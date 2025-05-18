import sys
import pygame

class Character:

	def __init__(self):

		pygame.init()
		# add screen
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Character")
		# add mario image
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('retro_mario.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill((0, 230, 0))
			self.screen.blit(self.image, self.rect)
			
			pygame.display.flip()

if __name__=='__main__':
	Character().run()