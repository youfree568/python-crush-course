while True:
	
	try:
		x = input('First number: ')
		if x == 'q':
			break

		x = int(x)

		y = input('Second number: ')
		if y == 'q':
			break

		y = int(y)
		
	except ValueError:
		print("Sorry, your input is not a number.")
	else:
		sum = x + y
		print(f"{x} + {y}  = {sum}")

