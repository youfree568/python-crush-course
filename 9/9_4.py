class Restaurant:
	"""Creat a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""attribute initialization"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""describe of the restaurant"""
		print(
			f"Our restaurant is called {self.restaurant_name},"
			f" this restaurant serves {self.cuisine_type} cuisine."
			)

	def open_restaurant(self):
		"""informs that our restaurant is open"""
		print(f"{self.restaurant_name} is open now!")

	def set_number_served(self, set_served):
		"""Set how much client we served"""
		if set_served >= 0:
			self.number_served = set_served
		else:
			print(f"Your input is negative.")

	def increment_number_served(self, new_served):
		"""add new served client"""
		if new_served > 0:
			self.number_served += new_served
		else:
			print(f"You input negative number!")

dnister = Restaurant('Dnister', 'Ukranian')

dnister.set_number_served(5)
print(f"Our served client number: {dnister.number_served}")

dnister.increment_number_served(25)
print(f"Our served client number: {dnister.number_served}")
