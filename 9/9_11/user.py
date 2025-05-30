class User:
	"""take user information"""
	def __init__(self, first_name, surname, age, email):
		"""initialization"""
		self.first_name = first_name
		self.surname =surname
		self.age = age
		self.email = email
		self.login_attempts = 0

	def describe_user(self):
		"""shows usef info"""
		print(
			f"User info:\n\tfirst name: {self.first_name}"
			f"\n\tsurname: {self.surname}\n\tage: {self.age}\n\temail: {self.email}\n"
			) 

	def great_user(self):
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
	def __init__(self, first_name, surname, age, email):
		super().__init__(first_name, surname, age, email)
		
		"""initialization list of privileges"""
		self.privileges = Privileges()

	
class Privileges:
	"""Show priviliges"""
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		"""show preveligious"""
		if self.privileges:
			print("\nUser have Privileges:")
			for privilege in self.privileges:
				print(f"\t- {privilege}")
		else:
			print("This user has no privileges!")