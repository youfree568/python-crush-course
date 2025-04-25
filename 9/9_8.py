class User:
	"""опис користувача"""
	def __init__(self, first_name):
		""" initialization"""
		self.first_name = first_name
		self.login_attempts = 0

	def describe_user(self):
		print(f"This is {self.first_name}") 

	def greet_user(self):
		print(f"Hello, {self.first_name}")

	def increment_login_attempts(self):
		"""Increment the value of login_attempts"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""reset login_attempts to 0"""
		self.login_attempts = 0


class Admin(User):
	"""initialization """
	def __init__(self, first_name):
		"""наслідування User"""
		super().__init__(first_name)
		"""Екземпляр (клас) Privileges як атрибут для класу адмін"""
		self.privileges = Privileges()

	
class Privileges:
	"""клас який показує переваги"""
	def __init__(self, privi=[]):
		self.privi = privi

	def show_privileges(self):
		"""show the user what the Admin can do"""
		for privilege in self.privi:
			print(f"\t- {privilege}")


nick = Admin('Admin')
nick.privileges.privi = ('can add post', 'can delete post', 'can ban user')
nick.privileges.show_privileges()