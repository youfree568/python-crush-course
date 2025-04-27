from car import Car
from electric_car import ElectricCar as ecar

my_audi = Car("Audi", "A7", 2025)
print(my_audi.get_descriptive_name())
my_bmw = Car("Bmw", "m5", 2025)
print(my_bmw.get_descriptive_name())
my_tesla = ecar("Tesla", "model s", 2025)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
