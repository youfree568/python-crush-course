filename = 'text_files\\learning_python.txt'

with open(filename) as file_object:
	text = file_object.read()

print(text)

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

with open(filename) as file_object:
	lines = file_object.readlines()

python_can = ''

for line in lines:
	python_can += line

print(python_can)