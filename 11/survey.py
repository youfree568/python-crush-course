class AnonymousSurvey:
	"""colect anonymous answers and questions"""
	def __init__(self, question):
		"""save question and prepare to saving answers"""
		self.question = question
		self.responses = []

	def show_question(self):
		print(self.question)

	def store_response(self, new_response):
		"""save one answer to one question"""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all answers"""
		print("Survey results:")
		for response in self.responses:
			print(f"- {response}")