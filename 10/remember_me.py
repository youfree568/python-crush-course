import json

username = input("What is your name? ")	

filename = 'json_files\\username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username.title()}!")