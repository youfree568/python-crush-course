from random import randint

class Die:
	"""create playing cube"""
	def __init__(self, sides=6):
		"""initialization"""
		self.sides = sides

	def roll_die(self):
		"""make die roll"""
		return randint(1, self.sides)


# make and roll die whit 6 sides
my_die_6 = Die()
results = []
for _ in range(10):
	result = my_die_6.roll_die()
	results.append(result)

print(results)

# make and roll die whit 10 sides
my_die_10 = Die(sides=10)

results = []
for _ in range(10):
	result = my_die_10.roll_die()
	results.append(result)

print(results)

# make and roll die whit 20 sides
my_die_20 = Die(sides=20)

results = []
for _ in range(10):
	results.append(my_die_20.roll_die())

print(results)