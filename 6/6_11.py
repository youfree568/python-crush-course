cities = {
	'kyiv': {
		'location': 'ukraine',
		'population': '2.9b',
		'fact': 'capital of ukraine',
	},

	'khmelnitskyi': {
		'location': 'ukraine',
		'population': '159t',
		'fact': 'faimouse bazar',
	},

	'ternopil': {
		'location': 'Ukraine',
		'population': '130t',
		'fact': 'faine misto',
	}
	}	


for city, info in cities.items():
	print(f"\n{city.title()}:\n\t{info['location'].title()}\n\t"
		f"population - {info['population']}\n\tfact: {info['fact']}")