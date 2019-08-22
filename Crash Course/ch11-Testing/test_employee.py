# CH11 Exercise 11-3
#
# test_employee.py
#
# Write two methods: test_give_default_raise() and test_give_custom_raise().
# Use setUp() method to create object only once
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test case class to validate Employee() class"""

    def setUp(self):
        """Create single instance of Employee object"""
        self.person = Employee('peter', 'gregory', 500000)

    def test_give_default_raise(self):
        """Test give_raise() with no salary input"""
        # Give Peter Gregory a raise!
        self.person.give_raise()
        # Does Peter Gregory's salary equal 500000 + 5000?
        self.assertEqual(self.person.salary, 505000)

    def test_give_custom_raise(self):
        """Test give_raise() with a 10000 salary input"""
        self.person.give_raise(10000)
        self.assertEqual(self.person.salary, 510000)


# Run test case
unittest.main()
