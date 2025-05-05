name = input('What is your name?\nName: ')

filename = 'text_files\\customer_name.txt'

with open(filename, 'a') as file_object:
	file_object.write(f"\ncustomer name - {name}")