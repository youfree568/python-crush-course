active = True
while active:
	age = input(f"What is your age?\nAge: ")
	if age == 'quit':
		active = False
	age = int(age)

	if age < 3:
		print('Free ticket!')
	elif age < 13:
		print('Ticket 10$')
	elif age >= 13:
		print('Ticket 15$')

