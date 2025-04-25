def city_country(city, country):
	correct = f"{city}, {country}"
	return correct.title()

print(city_country(country='ukraine', city='lwiw'))
print(city_country('khmelnytskyi', 'ukraine'))
print(city_country(city='warsaw', country='poland'))