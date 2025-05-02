from random import choice

lottery_numbers = (
	'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
	)

win_ticket = []
for i in range(4):
	result = choice(lottery_numbers)
	win_ticket.append(result)

print(f"wining ticket is: {win_ticket}")

