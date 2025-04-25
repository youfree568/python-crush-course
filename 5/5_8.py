'''HELLO ADMIN'''

names = ['admin', 'nick', 'mick', 'john', 'bob']
string = 'how are you?'
for name in names:
	if name == 'admin':
		print(f"Hello {name}, would you like to see a status report?")
	else:
		print(f"Hello {name.capitalize()}, thank you for loggin in again.")