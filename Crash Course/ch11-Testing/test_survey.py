# CH11 Example
#
# test_survey.py
#
# Testing the class in survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test the class AnonymousSurvey"""

    # This method is imported from unittest.TestCase.  It sets up the my_survey
    # object once for both test_ methods to use below
    def setUp(self):
        """
        Create a survey and set a list of responses for use in all test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'spanish', 'mandarin']


    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    # Create a test method for storing multiple responses
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        # Assert that all responses exist in responses list
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
