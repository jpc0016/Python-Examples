# CH11 Example
#
# survey.py
#
# Testing a class
# Python has many more assert methods for unit Testing
# Write a sample class to test

class AnonymousSurvey():
    """Collect anonymous answers to a survey question"""

    def __init__(self, question):
        """Store a question and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Display the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the question"""
        self.responses.append(new_response)

    def show_results(self):
        """Display all results of survey question given"""
        print("Survey Results: ")
        for response in self.responses:
            print('- ' + response)
