import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage devices fired by Paimon"""
	
	def __init__(self, slime_settings, screen,paimon):
		
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,slime_settings.bullet_width, slime_settings.bullet_height)
		self.rect.centerx = paimon.rect.centerx
		self.rect.top = paimon.rect.top

		self.y = float(self.rect.y)
		self.color = slime_settings.bullet_color
		self.speed_factor = slime_settings.bullet_speed_factor

	def update(self):

		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color, self.rect)
		