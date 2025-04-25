class Restaurant:
	"""опис ресторану"""

	def __init__(self, restaurant_name, cuisine_type):
		"""ініціалізувати атрибути"""
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		print(f"This is '{self.name}' restaurant!")
		print(f"He have kitchen of {self.type}.")

	def open_restaurant(self):
		print(f"Now, restaurant '{self.name}' is open!")

res = Restaurant("Пузата хата", "український фастфуд")

# print(res.name, res.type)
# res.describe_restaurant()
# res.open_restaurant()


