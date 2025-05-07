try:
	x = int(input('First number: '))
	y = int(input('Second number: '))
except ValueError:
	print("Sorry, your input is not a number.")
else:
	print(f"Your first number is {x}\nYour second number is {y}")

