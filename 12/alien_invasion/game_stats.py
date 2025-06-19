class GameStats:

	"""game statistic"""

	def __init__(self, ai_game):
		"""initialization"""
		self.settings = ai_game.settings
		self.reset_stats()
		# start game in active status
		self.game_active = True

	def reset_stats(self):
		"""initialization statistic"""
		self.ship_left = self.settings.ship_limit