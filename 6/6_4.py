glossary = {
	'string': 'послідовність символів',
	'list': 'набір елементів у певному порядку',
	'loop': 'обробляє набір елементів у певному порядку',
	'comment': 'примітка в програмі яку інтерпритатор ігнорує',
	'dictinary': 'колекція пар ключ-значення',
	'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
}

for key, values in glossary.items():
	print(f"\n{key.title()}: {values}")