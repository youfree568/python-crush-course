class Restaurant:
	"""Creat a restaurant"""
	def __init__(self, name, cuisine_type):
		"""attribute initialization"""
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""describe of the restaurant"""
		print(
			f"Our restaurant is called {self.name},"
			f" this {self.cuisine_type} cuisine."
			)

	def open_restaurant(self):
		print(f"{self.name} is open now!")