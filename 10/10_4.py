filename = 'text_files\\guest_book.txt'

name = ''
while True:
	name = input('What is your name?\n')
	if len(name) > 0:	
		if name == 'q' or name == 'quit':
			print('You want to quit!\nBye!')
			break
		else:
			print(f"Hello, {name.title()}\n")
			with open(filename, 'a') as file_object:
				file_object.write(f"{name.title()}\n")
	else:
		print('Please singh your name.')