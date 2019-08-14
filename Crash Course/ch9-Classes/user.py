# CH9 Exercise 9-3
#
# user.py
#
# Creating a class called user.  __init__() has two attributes: first_name and
# last_name.  Make other attributes typically stored in a user profile.  Make
# method that prints summary of attributes.  Make method that prints
# a personal greeting to the user.
class User():
    """
    User profile class that stores a web user's pertinent information.
    Includes two methods: describe_user() and greet_user()
    """

    # Set default blank value for age since age is optional parameter
    def __init__(self, first_name, last_name, **user_info):
        """Sets variables to self instance"""
        self.first_name = first_name
        self.last_name = last_name

        # Similar to Exercise 8-13 user_profile-2.py except the dictionary is
        # an attribute of self.
        self.attributes = {}
        for key,value in user_info.items():
            self.attributes[key] = value
            # self.key = value

    def describe_user(self):
        """Displays user attributes"""
        print("First name: " + self.first_name.title() +
                "\nLast name: " + self.last_name.title())
        for key,value in self.attributes.items():
            print(str(key.title()) + ": " + str(value))

    def greet_user(self):
        """Print greeting to user"""
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

# Create user
person = User('john', 'smith', age=9, username='dudebro55', location='brazil')
person.describe_user()
print(" ")
person.greet_user()
