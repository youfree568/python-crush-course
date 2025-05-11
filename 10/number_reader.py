import json

filename = 'json_files\\numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)