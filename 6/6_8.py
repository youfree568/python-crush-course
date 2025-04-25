pet_1 = {
	'type': 'cat',
	'name': 'kica',
	'owner_name': 'jack'
}
pet_2 = {
	'type': 'dog',
	'name': 'spike',
	'owner_name': 'bob'
}

pet_3 = {
	'type': 'kangaroo',
	'name': 'tyson',
	'owner_name': 'mick'
}

pets = [pet_1, pet_2, pet_3]

print(pets)

# for i in pets:
# 	print(f"Here's what I know about {i['name'].title()}")
# 	for key, values in i.items():
# 		print(f"\t{key}: {values}")


for i in pets:
	print(f"What I know about this animal:\n\t{i['type']}, named "
		f"{i['name'].title()}, owner name {i['owner_name'].title()}")