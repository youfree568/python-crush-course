name = ['Schwarzenegger', 'Stalone', 'Tarantino']
lost_name = name.pop(2)
name.append('Bread')
print(f'Hello, {name[0]} nice to see you.')
print(f'Hello, {name[1]} nice to see you.')
print(f"Hello, {lost_name} can't to came.")
print(f'Hello, {name[2]} nice to see you.')
name[2] = 'Bean'
print(f'Hello, {name[2]} nice to see you.')

