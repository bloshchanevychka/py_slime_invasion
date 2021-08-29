import pygame

class Paimon(object):
	"""attacing Slime"""
	def __init__(self, screen,slime_settings):
		self.screen = screen 
		self.slime_settings = slime_settings
		self.image = pygame.image.load('images\\paimon.png').convert_alpha()
		self.image = pygame.transform.smoothscale(self.image, (70, 70))
		self.direction = "right"

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.center = float(self.rect.centerx)
		self.rect.bottom = self.screen_rect.bottom
		self.vert = float(self.rect.bottom)
		#self.rect.left = self.screen_rect.left
		#self.rect.centery = self.screen_rect.centery

	def update(self):

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.slime_settings.paimon_speed_factor
			self.direction = "right"
		if self.moving_left and self.rect.left > 0:
			self.center -= self.slime_settings.paimon_speed_factor
			self.direction = "left"		
		if self.moving_up and self.rect.top > 0:
			self.vert -= self.slime_settings.paimon_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.vert += self.slime_settings.paimon_speed_factor
			
		self.rect.centerx = self.center
		self.rect.bottom = self.vert

	def blitme(self):

		if self.direction == "right":
			self.screen.blit(self.image,self.rect)
		elif self.direction == "left":
			self.screen.blit(pygame.transform.flip(self.image,True, False), self.rect)

	def center_paimon(self):
		self.center = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.vert = float(self.rect.bottom)