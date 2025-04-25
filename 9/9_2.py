class Restaurant:
	"""Creat a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""attribute initialization"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""describe of the restaurant"""
		print(
			f"Our restaurant is called {self.restaurant_name},"
			f" this restaurant serves {self.cuisine_type} cuisine."
			)

	def open_restaurant(self):
		print(f"{self.restaurant_name} is open now!")


dnister = Restaurant('Dnister', 'Ukranian')
peperoni = Restaurant('Peperoni', "Italian")
baguette = Restaurant('Baguette', 'French')

dnister.describe_restaurant()
peperoni.describe_restaurant()
baguette.describe_restaurant()
