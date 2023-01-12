import pygame.font
# creating test branch 2 for conflict
class Button(object):
	"""docstring for Button"""
	def __init__(self, slime_settings, screen, msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.width, self.height = 200, 50
		self.button_color = (0, 255, 120)
		self.txt_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_img = self.font.render(msg, True, self.txt_color, self.button_color)
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_img, self.msg_img_rect)

