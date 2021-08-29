import pygame
from pygame.sprite import Sprite
from random import randint

class Slime(Sprite):
	"""A slime from Slime army!"""

	def __init__(self, slime_settings, screen):
		super().__init__()
		self.screen = screen
		self.slime_settings = slime_settings
		self.image = self.slime_settings.slimes[randint(0,len(slime_settings.slimes) - 1)]

		self.image = pygame.image.load(self.image).convert_alpha()		
		self.image = pygame.transform.smoothscale(self.image, self.slime_settings.slime_size)
		self.rect = self.image.get_rect()
		self.rect.x = int(self.rect.width/2)
		self.rect.y = int(self.rect.height/4)

		self.x = float(self.rect.x)

	def check_edges(self):
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += (self.slime_settings.slime_speed_factor * self.slime_settings.slimes_direction)
		self.rect.x = self.x