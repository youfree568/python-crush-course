import json

# Load username, if it exist
# if not write username to file
filename = 'json_files\\username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")	
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username.title()}!")
else:
	print(f"Welcome back, {username.title()}")