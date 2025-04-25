people = []

person_1 = {
	'first_name': 'Nick',
	'last_name': 'Smith',
	'age': 10,
	'city': 'New York',
}

# people.append(person)

person_2 = {
	'first_name': 'mick',
	'last_name': 'tmith',
	'age': 22,
	'city': 'london',
}

# people.append(person)

person_3 = {
	'first_name': 'bob',
	'last_name': 'Smith',
	'age': 33,
	'city': 'paris',
}

# people.append(person)

people = [person_1, person_2, person_3]

for i in people:
	name = f"{i['first_name'].title()} {i['last_name'].title()}"
	age = i['age']
	city = i['city'].title()

	print(f"{name}, from {city}, is {age} year old.")