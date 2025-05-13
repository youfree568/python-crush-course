from survey import AnonymousSurvey

# define questions and create survey
question = "What lanuage did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show questions and save answers
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)


# Show survey result
print("\nThank you to everyone who paricipated in the survey!")
my_survey.show_results()