currents_users = ['admin', 'nick', 'bill', 'john', 'bob']
new_users = ['new', 'old', 'bill', 'bo', 'bob']

currents_users_lower = [user.lower() for user in currents_users]

for user in new_users:
	if user.lower() in currents_users_lower:
		print("You must choose another name!")
	else:
		print("This name is free.")

# print(new_users.upper())