# CH8 Example
#
# greeter.py
#
# Intro to functions.
# Simple greeter function

# Uses 'def' keyword.
def greet_user(name):
    """docstring"""
    print("Hello, " + name.title() + "!")

# Can call function multiple times!
greet_user("jared")
greet_user("mike")
greet_user("gilfoyle")
greet_user("henry")
