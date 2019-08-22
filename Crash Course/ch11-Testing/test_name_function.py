# CH11 Example
#
# test_name_function.py
#
# Import unittest module to run test cases on get_formatted_name()
import unittest
from name_function import get_formatted_name

# Create class that contains series of tests for get_formatted_name().  Can be
# named anything.  Must inherit from unittest.TestCase class in module unittest.
class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # Asserting that formatted_name equals 'Janis Joplin'
        self.assertEqual(formatted_name, 'Janis Joplin')

    # Test for middle name functionality
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()

# Output for first and last name only:
    # .
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.000s
    #
    # OK


# Changing the function in name_function.py to accept a middle name causes the test
# case to fail.  Output is below:
    # E
    # ======================================================================
    # ERROR: test_first_last_name (__main__.NameTestCase)
    # Do names like 'Janis Joplin' work?
    # ----------------------------------------------------------------------
    # Traceback (most recent call last):
    #   File "test_name_function.py", line 16, in test_first_last_name
    #     formatted_name = get_formatted_name('janis', 'joplin')
    # TypeError: get_formatted_name() missing 1 required positional argument: 'last'
    #
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.000s
    #
    # FAILED (errors=1)
