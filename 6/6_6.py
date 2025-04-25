favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = []

for key in favorite_languages.keys():
    people.append(key)

another = ['bob', 'nina', 'john',]

people = people + another
print(people)

for name in people:
    if name in favorite_languages:
        print(f"Thank you for taking the poll {name.title()}\n")
    else:
        print(f"{name.title()}, what is your favorite language?\n")