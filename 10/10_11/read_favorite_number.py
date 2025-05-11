import json

filename = r'D:\coding\2024\python_work\10\json_files\favorit_number.json'
with open(filename) as f:
	read_number = json.load(f)
	print(f"I know your favorite number! It's {read_number}")