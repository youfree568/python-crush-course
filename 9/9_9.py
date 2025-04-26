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
		else:
			range = "to the mooooooooooooon like"

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""make battery more powerfull"""
		if self.battery_size < 100:
			self.battery_size = 100
			print("Your battery upgrade to 100kWh.")
		elif self.battery_size == 100:
			print("Your battery is upgrade before and have 100kWh.")
		elif self.battery_size > 100:
			print("Your battery is more powerful than we can do!")


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

# my_electrocar = ElectricCar('Polestar', 'model 2', 2025)
# print(my_electrocar.get_descriptive_name())
# my_electrocar.battery.describe_battery()
# my_electrocar.battery.get_range()

electrocar = ElectricCar('Nissan', 'Nismo', 2025)
electrocar.battery.get_range()
electrocar.battery.upgrade_battery()
electrocar.battery.get_range()
electrocar.battery.battery_size = 101
electrocar.battery.get_range()
electrocar.battery.upgrade_battery()