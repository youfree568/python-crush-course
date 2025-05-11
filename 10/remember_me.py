import json

def get_stored_username():
	"""Take a name if it exist"""
	filename = 'json_files\\username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""asked username"""
	username = input("What is your name? ")
	filename = 'json_files\\username.json'	
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""greeting user"""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username.title()}")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()