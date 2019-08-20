# CH9 Exercise 9-11
#
# call_admin.py
#
# Creating a class instance of Admin by importing it from admin.py.
# Call show_privileges() method to show functionalityca
from admin import Admin

# Note: admin.py is another example and not a standalone module.  Comment out the
# bottom lines of admin.py before running this example.
jeff = Admin('jeff', 'starr')
jeff.describe_user()
print(" ")
jeff.privileges.show_privileges()
