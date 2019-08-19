# CH9 Exercise 9-6
#
# ice-cream.py
#
# Creating an ice cream stand class that is a specific kind of restaurant.
# IceCreamStand() inherits from Restaurant().  Add flavors attribute for a list
# of ice cream flavors.  Add method to display flavors

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


# New subclass of restaurant called IceCreamStand()
class IceCreamStand(Restaurant):
    """Type of restaurant that specifically serves ice cream"""

    def __init__(self, restaurant_name, cuisine_type='ice-cream'):
        """Initialize name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def show_flavors(self):
        """prints ice cream flavors"""
        print("Avaliable flavors: ")
        for flavor in self.flavors:
            print("\t" + flavor.title())

# Create instance of IceCreamStand() then display flavors with method.
coldstone = IceCreamStand('coldstone')
coldstone.show_flavors()
