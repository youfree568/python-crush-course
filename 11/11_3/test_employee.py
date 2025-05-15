import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		
		self.employee = Employee('mykola', 'ovcharuk', 20_000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 25000)

	def test_give_custom_raise(self):
		self.employee.give_raise(10_000)
		self.assertEqual(self.employee.salary, 30_000)

if __name__=='__main__':

	unittest.main()