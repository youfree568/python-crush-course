class Settings:
	"""Saves all settings to alien_invasion.py"""

	def __init__(self):
		"""initialization"""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.ship_speed = 2

		# Bullet settings
		self.bullet_speed = 3
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 5

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction = 1 (move right), fleet_direction = -1 (move left)
		self.fleet_direction = 1