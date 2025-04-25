pizza = []

while True:
	# pizza = []
	ing = input()

	if ing == 'quit':
		break
	elif ing == ' ':
		continue
	pizza.append(ing)
	print("Наша піца містить: ")
	for i in pizza:
		print(f"\t{i}")