filename = 'text_files\\learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

replaces = ''
for line in lines:
	replaces += line
print(replaces.replace('python', 'C'))