"""car modeling class"""

class Car:
	"""make a car"""
	def __init__(self, make, model, year):
		"""initialization"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""return full information about car"""
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name.upper()

	def read_odometer(self):
		"""Show odometer mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""update mileage if it not roll back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add miles to odometer"""
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print(f"You can't roll back mileage!")