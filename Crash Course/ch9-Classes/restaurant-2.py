# CH9 Exercise 9-1 and 9-2
#
# restaurant-2.py
#
# Creating a restaurant class.  __init__() has two attributes: name and
# cuisine type.  Make method that prints both attributes.  Make method that
# prints "restaurant is open"

class Restaurant():
    """
    Restaurant class with two attributes and two methods
    """

    # __init__() purpose is to initialize the variables into object "self"
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Follow-on methods only require "self" to be passed, but referencing attributes
    # requires dot notation
    def describe_restaurant(self):
        """Simple restaurant description"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " style restaurant.")

    def open_restaurant(self):
        """Indicate restaurant is open"""
        print("We are open for business!")


mexican_restaurant = Restaurant('Casa Blanca', 'Mexican')

# Print both attributes individually
print(mexican_restaurant.restaurant_name)
print(mexican_restaurant.cuisine_type)

# Run both methods
mexican_restaurant.describe_restaurant()
mexican_restaurant.open_restaurant()

# Exercise 9-2
# Creat 3 different instances of a Restaurant
italian_restaurant = Restaurant('terranovas', 'italian')
italian_restaurant.describe_restaurant()

burgers = Restaurant('red robin', 'burger')
burgers.describe_restaurant()
