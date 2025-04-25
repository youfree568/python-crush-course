def show_messages(one):
	for i in one:
		print(i)

def send_messages(messages):
	while messages:
		current_message = messages.pop()
		sent_messages.append(current_message)
		print(current_message)

messages = [
	'hello', 'nice', 'ok', 'end',	
]

sent_messages = []
send_messages(messages[:])
print(messages)