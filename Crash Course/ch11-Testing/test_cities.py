# CH11 Exercise 11-1 and 11-2
#
# test_cities.py
#
# Write a method test_city_country() to verify calling the function results in
# the correct string
import unittest
from city_functions import city_country

class TestCityCase(unittest.TestCase):
    """Test case to ensure city_country() returns the proper string"""

    def test_city_country(self):
        """Test the city_country() function for expected output"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    # New method to test city, country, and population
    def test_city_country_population(self):
        """Test the city_country() function for expected output"""
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


# Don't forget to run 'unittest.main()' to execute test cases
unittest.main()
