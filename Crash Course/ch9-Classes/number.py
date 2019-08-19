# CH9 Exercise 9-4
#
# number.py
#
# Start with restaurant-2.py.
# Add an attribute called number_served with default value of 0.  Print number
# of customers the restaurant has served, then change the value and print again.
# Add method called set_number_served() to set a starting point
# Add method called increment_number_served() to increment amount of customers
# served.

class Restaurant():
    """
    Restaurant class with two attributes and two methods
    """

    # __init__() purpose is to initialize the variables into object "self"
    # added number_served attribute
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize name and cuisine variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    # Follow-on methods only require "self" to be passed, but referencing attributes
    # requires dot notation
    def describe_restaurant(self):
        """Simple restaurant description"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " style restaurant.")

    def open_restaurant(self):
        """Indicate restaurant is open"""
        print("We are open for business!")


    def set_number_served(self, customers):
        """Set number of customers that have been served"""
        self.number_served = customers

    def increment_number_served(self, customers):
        """Increment number of customers served by a certain amount"""
        self.number_served += customers


# Create restaurant object
restaurant = Restaurant('Casa Blanca', 'Mexican')

# Print number of customers the restaurant has served
print("Customers served today: " + str(restaurant.number_served))

# Call set_number_served with a value and print it
restaurant.set_number_served(50)
print("Customers served today: " + str(restaurant.number_served))

# Call increment_number_served with a value and print it
restaurant.increment_number_served(200)
print("Customers served today: " + str(restaurant.number_served))
