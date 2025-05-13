import unittest
from city_function import city_country

class NameTestCase(unittest.TestCase):
	"""test for city_function"""
	def test_city_country(self):
		"""result must be something like that 'Santiago, Chily'"""
		city_location = city_country('santiago', 'chily')
		self.assertEqual(city_location, 'Santiago, Chily')

	def test_city_country_population(self):
		"""check "Santiago, Chily - population = 500000"""
		city_population = city_country('santiago', 'chily', 5000000)
		self.assertEqual(city_population, 'Santiago, Chily - population 5000000')

if __name__=='__main__':
	unittest.main()