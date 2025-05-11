import json

filename = r'D:\coding\2024\python_work\10\json_files\favorit_number.json'
username = input("What is your favorite number? ")

with open(filename, 'w') as f:
	json.dump(username, f)