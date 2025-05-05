filename = 'text_files\\answers.txt'
count = 0

while True:
	answer = input("Why do you like programming?\n")
	if len(answer) > 0:
		if answer == 'q':
			print('You want to leave!\nBye!')
		else:
			print("Thank you for your answer!\n")	
			count += 1
			with open(filename, 'a') as file_object:
				file_object.write(f"{count}. {answer}\n")
	else:
		print("Please, write something!")