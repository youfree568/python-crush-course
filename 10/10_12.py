import json

def read_fav_number():
	filename = 'json_files\\favorit_number.json'
	try:
		with open(filename) as f:
			user_number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return user_number

def get_fav_number():
	user_number = input("What is your favorite number? ")
	filename = r'json_files\favorit_number.json'

	with open(filename, 'w') as f:
		json.dump(user_number, f)
	return user_number

def show_fav_number():
	favorit_number = read_fav_number()
	if favorit_number:
		print(f"I know your favorite number! It's {favorit_number}")
	else:
		favorit_number = get_fav_number()
		print(f"Ok, your favorite number is {favorit_number}")

show_fav_number()