def city_country(city, country, population=''):
	"""shows to us name of city and country"""
	if population:
		return f"{city.title()}, {country.title()} - population {population}"
	else:
		return f"{city.title()}, {country.title()}"