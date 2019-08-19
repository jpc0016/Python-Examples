# CH9 Exercise 9-7 and 9-8
#
# admin.py
#
# Creating a class called Admin that inherits from User.  Add attribute called
# privileges that stores strings like "can add post", "can delete post", "can
# ban user"  Write show_privileges() method to display privileges
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

# Create Admin() class with inheritance from User()
class Admin(User):
    """A special user that can take special actions"""

    def __init__(self, first_name, last_name, **user_info):
        """Initialize self variable of Admin"""
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()



# Create Privileges() class that supplies Admin() class with an instance
class Privileges():
    """Class instance that describes elevated rights"""

    def __init__(self):
        """Initialize list of privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """List Administrator's set of privileges"""
        print("Admin privileges: ")
        for privilege in self.privileges:
            print("\t" + privilege)



# Create admin class and list privileges
person = Admin('john', 'smith', age=9, username='dudebro55', location='brazil')
person.describe_user()
print(" ")
# privileges is lowercase since it refers to Admin attribute on line 45
person.privileges.show_privileges()
