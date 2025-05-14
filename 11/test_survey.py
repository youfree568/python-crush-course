import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for AnonymousSurvey class"""

	def test_store_single_response(self):
		"""Check if one answer saved corectly"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		"""check if 3 individual responses saves corectly"""
		question = 'What language did you first learn to speak?'
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Polish', 'German']
		for response in responses:
			my_survey.store_response(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)


if __name__=='__main__':
	unittest.main()