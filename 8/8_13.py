def build_profile(first, last, **user_info):
	"""Створити словник, що міститиме всю інформацію про користувача"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Mykola', 'Ovcharuk', 
								location='Gdansk',
								age=33,
								sex='male')

print(user_profile)