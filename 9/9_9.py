class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	"""battery description"""
	def __init__(self, battery_size=75):
		"""initialization"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Share info about battery size"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):

		"""show how far you can go"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 360

		print(f"This car can go about {range} miles on a full charge.")


	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100
			print('Upgrade battery to 100kw')

class ElectricCar(Car):
	
	def __init__(self, make, model, year):
		"""Наслідування класу"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		"""specification"""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('Tesla', 'S', 2020)

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()