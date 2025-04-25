favorit_numbers = {
	'Nick': [33, 22],
	'Marta': [23, 44], 
	'Bob': [2, 77],
	'Linda': [9, 87],
	'Monika': [999, 888, 777],
}

for a, b in favorit_numbers.items():
	print(f"\n{a.title()} favorit numbers is:")
	for i in b:
		print(f"\t{i}")