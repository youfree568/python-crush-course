def make_car(car, model, **info):
	# car_info['car_brand'] = car

	# print(f"My car is {car} {model}, she is {color}")
	info['brand'] = car
	info['car_model'] = model

	for a, b in info.items():
		print(a, b)
	return info
my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
