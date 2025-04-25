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

class IceCreamStand(Restaurant):


	def __init__(self, restaurant_name, cuisine_type):
		"""initialization"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def sort_of_icecream(self):
		"""show list of icecream taste"""
		print(f"We have this type of icecream:")
		for flavor in self.flavors:
			print(f"\t- {flavor} icecream")

icecreamvan = IceCreamStand('Happy ours', 'ice cream')
icecreamvan.flavors = ['vanilla', 'chocolate', 'strawbarry']

icecreamvan.describe_restaurant()
icecreamvan.sort_of_icecream()


