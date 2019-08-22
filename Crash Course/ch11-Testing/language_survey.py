# CH11 Example
#
# language_survey.py
#
# Testing the class in survey.py

from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"

my_question = AnonymousSurvey(question)

# Show the question and store the response to the question
my_question.show_question()
print("Enter 'q' at any time to quit. \n")

while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    else:
        my_question.store_response(response)

# Show survey response
print("Thank you to everyone who participated in the survey! ")
my_question.show_results()
