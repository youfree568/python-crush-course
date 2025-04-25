class Dog:
	"""simple attempt to model a dog"""
	def __init__(self, name, age):
		"""attribute initilialization name and age"""
		self.name = name
		self.age = age

	def sit(self):
		"""simulate the execution of 'sit' command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""sumulate the execution of 'roll over' command"""
		print(f"{self.name} rolled over!")



my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(
	f"\nYour dog's name is {your_dog.name} and"
	f"she is {your_dog.age} years old."
	)
your_dog.sit()