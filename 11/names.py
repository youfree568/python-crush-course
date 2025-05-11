from name_function import get_formatted_name

print("Enter 'q' if you want to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		print('Bye!')
		break
	last = input("\nPlease give me a first name: ")
	if last == 'q':
		print('Bye!')
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tNeatly formatted name: {formatted_name}")