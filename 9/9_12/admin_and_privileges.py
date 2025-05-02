from user import User

class Admin(User):
	"""This is SuperUser"""
	def __init__(self, first_name, surname, age, sex):
		super().__init__(first_name, surname, age, sex)
		
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