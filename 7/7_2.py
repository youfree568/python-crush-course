guests = input("Hello, how many guests do you have?\nGuests: ")
guests = int(guests)
if guests and guests > 0 and guests <= 8:
	print("Your table is ready!")
elif guests and guests > 8:
	print("Sorry, you have to wait!")
else:
	print("Please, specify the number of guests!")