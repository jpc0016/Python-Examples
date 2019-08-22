# CH11 Exercise 11-3
#
# employee.py
#
# Write class called Employee with first and last names and annual salary.  Write
# method give_raise() that adds $5000 to annual salary by default
class Employee():
    """Object representing an employee and salary"""

    def __init__(self, first_name, last_name, salary):
        """Initialize employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, bonus=''):
        """
        Method to give raise (bonus) to employee.  $5000 is the default amount.
        """
        if bonus:
            self.salary += bonus
        else:
            self.salary += 5000
