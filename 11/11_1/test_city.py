import unittest
from city_function import location

class NameTestCase(unittest.TestCase):
	"""test for city_function.py"""

	def test_city_country_location(self):
		"""Check if it work with places like 'santiago' , 'chile'"""
		location_place = location('santiago', 'chile')
		self.assertEqual(location_place, 'Santiago, Chile')

if __name__=='__main__':
	unittest.main()		