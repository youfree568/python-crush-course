from car import Car

my_new_car = Car("Mercedes", "AMG", 2025)

my_new_car.read_odometer()
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 30
my_new_car.read_odometer()