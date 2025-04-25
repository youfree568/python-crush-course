name = ['Schwarzenegger', 'Stalone', 'Tarantino']
name.insert(0, 'King')
name.insert(1, 'Usyk')
lost_name = name.pop(2)
name.append('Bread')
print(f'Hello, {name[0]} nice to see you.')
print(f'Hello, {name[1]} nice to see you.')
print(f"Hello, {lost_name} can't to came.")
print(f'Hello, {name[2]} nice to see you.')
name[2] = 'Bean'
print(f'Hello, {name[2]} nice to see you.')
print(f"Hello, {', '.join(name)}, i happy to see you all.\nWe have bigger table"
		" to meet all togheter.")
for i in name:
	print(f"We wait for you mr. {i} at 18:00 on Saturday this week.")
