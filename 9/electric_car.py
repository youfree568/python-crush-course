"""classes that can model electric car."""

from car import Car

class Battery:
	"""information about the battery"""

	def __init__(self, battery_size=75):
		"""initialization battery attribute"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""show size of car battery"""
		print(f"This car has a {self.battery_size}-kW battery.")
	
	def get_range(self):
		"""What distance battery can gives you"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
	"""properties of an electric car"""

	def __init__(self, make, model, year):
		"""parent attributes then
			add info about car only for 'electric car' """
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		"""Electric car don't have gas tank"""
		print(f"This car doesn't need a gas tank!")