from random import choice

lottery_ticket = (
	'a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
	)

winning_numbers = []

# for not using the same numbers we use while loop

while len(winning_numbers) < 4:

	lottery_number = choice(lottery_ticket)

	if lottery_number not in winning_numbers:
		winning_numbers.append(lottery_number)
		print(f"We pulled a {lottery_numbers}")

print(f"Winning ticket is: {winning_numbers}")