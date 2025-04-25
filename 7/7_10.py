responses = {}
question = True

while question:
	name = input('What is you name?\n\t')
	repeat = input("Can I ask you?")
	if repeat == 'no':
		question = False
	else:
		response = input('What is your favorit country?\n\t')
		responses[name] = response

for name, response in responses.items():
	print(f"{name.title()}'s favorit country is {response.title()}")