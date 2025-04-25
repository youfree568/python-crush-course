class User:
	"""take user information"""
	def __init__(self, first_name, surname, age, sex):
		"""initialization"""
		self.first_name = first_name
		self.surname =surname
		self.age = age
		self.sex = sex
		self.login_attempts = 0

	def describe_user(self):
		"""shows usef info"""
		print(
			f"User info:\n\tfirst name: {self.first_name}"
			f"\n\tsurname: {self.surname}\n\tage: {self.age}\n\tsex: {self.sex}\n"
			) 

	def greet_user(self):
		"""user greeting"""
		print(f"Hello {self.first_name}, nice to see you!\n")	

	def increment_login_attempts(self):
		"""add trying to login"""
		self.login_attempts += 1
		return self.login_attempts

	def reset_login_attempts(self):
		"""reset login attemps to '0' """
		self.login_attempts = 0
		return self.login_attempts


class Admin(User):
	"""This is SuperUser"""
	def __init__(self, first_name, surname, age, sex):
		super().__init__(first_name, surname, age, sex)
		self.privileges = []

	def show_privileges(self):
		"""show preveligious of Admin"""
		print(f"What can Admin: ")
		for privilege in self.privileges:
			print(f"\t- {privilege}")

super_user = Admin('Mykola', 'Admin', 33, 'male')
super_user.privileges = ['can add post', 'can delete post', 'can ban user']
super_user.show_privileges()