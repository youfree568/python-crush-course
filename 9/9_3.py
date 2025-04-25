class User:
	"""take user information"""
	def __init__(self, first_name, surname, age, sex):
		"""initialization"""
		self.first_name = first_name
		self.surname =surname
		self.age = age
		self.sex = sex

	def describe_user(self):
		"""shows usef info"""
		print(
			f"User info:\n\tfirst name: {self.first_name}"
			f"\n\tsurname: {self.surname}\n\tage: {self.age}\n\tsex: {self.sex}\n"
			) 

	def greet_user(self):
		"""user greeting"""
		print(f"Hello {self.first_name}, nice to see you!\n")	


user1 = User('Mykola', 'Ovcharuk', 33, 'male')
user2 = User('Yelyzaveta', 'Ovcharuk', 36, 'female')
user3 = User('Donna', 'Strange', 40, 'female')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()