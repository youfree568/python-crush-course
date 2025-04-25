places = {
	'bob': ['home', 'beach', 'garden'], 
	'nick': ['town'],
	'bill': ['lisabon', 'kipr'],
	}

for a, b in places.items():
	if len(b) == 1:
		print(f"\n{a.title()} favorit place is:")
		for i in b:
			print(i)
	else:
		print(f"\n{a.title()} favorit places is:")
		for i in b:
			print(i)