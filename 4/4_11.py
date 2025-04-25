pizza = ['4cheese', 'kapricoza', 'fruvita']
# for i in pizza:
# 	# print(f"I like {i} pizza")

# print('I really love pizza!')

friend_pizza = pizza[:]
pizza.append('peperonni')
friend_pizza.append('vulcano')
print(f"My favorite pizzas are:")
for i in pizza:
	print(i)

print("\nMy friend's favorite pizzas are:")
for i in friend_pizza:
	print(i)