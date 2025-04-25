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

print(f"Name of restaurant is {dnister.restaurant_name}.")
print(f"This restaurant serves {dnister.cuisine_type} cuisine.")

dnister.describe_restaurant()
dnister.open_restaurant()