def sandwich(*items):
	print('\nI make sandwich for you.')
	for item in items:
		print(f"I add {item} in your sandwich.")
	print("Here is your sandwich!")

sandwich('cheese', 'salat')
sandwich('ковбасу', 'сир', 'салат')
sandwich('оливки', 'сир - дорблю', 'салат', 'сосиски')