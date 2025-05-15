class Employee:

	def __init__(self, name, surname, salary):
		self.name = name
		self.surname = surname
		self.salary = salary

	def give_raise(self, raise_up=5000):
		self.salary += raise_up