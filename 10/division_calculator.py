print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		print("Bye!")
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		print("Bye!")
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(f"Answer is {answer}")