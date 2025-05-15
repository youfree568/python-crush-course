import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for AnonymousSurvey class"""

	def setUp(self):
		"""create a survey and set of responses for all tuning methods"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Polish', 'Germany']

	def test_store_single_response(self):
		"""Check if one answer saved corectly"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""check if 3 individual responses saves corectly"""

		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)


if __name__=='__main__':
	unittest.main()