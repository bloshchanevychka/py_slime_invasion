

class GameStats(object):
	"""docstring for GameStats"""
	def __init__(self, slime_settings):
		self.slime_settings = slime_settings
		self.game_active = False
		self.high_score = 0
		self.reset_stats()

	def reset_stats(self):
		self.lifes_left = self.slime_settings.lifes_limit
		self.score = 0
		self.level = 1
