from random import choice

numbers = [1, 2, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd']
my_ticket = [2, 4, 'd']
current_try = 0
won = False


def winner(numbers):
    # find winning ticket

    winning_ticket = []

    for i in range(3):
        result = choice(numbers)
        winning_ticket.append(result)
    return(winning_ticket)

while not won:
    # try to win a lottery
    lottery_ticket = winner(numbers)
    current_try += 1
    
    if lottery_ticket == my_ticket:
        won = True
        print(f'You won in {current_try} attempts.')