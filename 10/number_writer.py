import json

numbers = list(range(1, 20, 3))
print(numbers)

filename = 'json_files\\numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)