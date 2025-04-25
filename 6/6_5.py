river = {
	'dnipro': 'ukraine',
	'visla': 'poland',
	'dunai': 'german',
}

for key, values in river.items():
	print(f"{key.capitalize()} runs through {values.title()}!\n")

for key in river.keys():
	print(key)

for values in river.values():
	print(values)