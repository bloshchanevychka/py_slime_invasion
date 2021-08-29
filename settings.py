from os import getcwd, listdir
from os.path import isfile, join, abspath,exists
class Settings(object):
	"""here are stored all game settings"""

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 760
		self.bg_color = (60,60,60)

		# paimon settings
		self.lifes_limit = 3

		#bullet settings
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color =  100,240,100
		self.bullets_allowed = 5

		#slime settings
		self.slime_size = (60, 60)
		self.slimes_path = join(abspath(getcwd()), 'images', 'slimes')
		self.slimes = [join(self.slimes_path, slime_) for slime_ in listdir(self.slimes_path) 
		if  isfile(join(self.slimes_path, slime_)) and ('.png' in slime_ or '.bmp' in slime_)] 
		self.army_drop_speed = 10
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.paimon_speed_factor = 1.1
		self.bullet_speed_factor = 2
		self.slime_speed_factor = 0.3
		self.slimes_direction = 1 # -1 for moving <-, 1 for ->
		self.slime_points = 50	

	def increase_spead(self):
		self.paimon_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.slime_speed_factor *= self.speedup_scale
		self.slime_points = int(self.slime_points*self.score_scale)
		