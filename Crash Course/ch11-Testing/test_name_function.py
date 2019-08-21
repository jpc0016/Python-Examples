# CH11 Example
#
# test_name_function.py
#
# Import unittest module to run test cases on get_formatted_name()
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
