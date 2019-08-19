# CH9 Exercise 9-5
#
# user-2.py
#
# Start with user.py Exercise 9-3
#
# Add attribute called login_attempts.  Add method called increment_login_attempts().
# Add method called reset_login_attempts() to reset number of login attempts to
# zero

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
        self.attributes = {'login_attempts': 0}
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

    def increment_login_attempts(self):
        """Increments value of attribute login_attempts by 1"""
        self.attributes['login_attempts'] += 1

    def reset_login_attempts(self):
        """Resets value of login_attempts to zero"""
        self.attributes['login_attempts'] = 0


# Create user
person = User('john', 'smith', age=9, username='dudebro55', location='brazil')
person.describe_user()

# Test incrementing login attempts
print(" ")
person.increment_login_attempts()
person.describe_user()

print(" ")
person.increment_login_attempts()
person.describe_user()

# Check reset_login_attempts function and display
print(" ")
person.reset_login_attempts()
person.describe_user()

# Can print a single attribute like this:
print(person.attributes['login_attempts'])
