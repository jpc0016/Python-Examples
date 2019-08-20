# CH9 Example
#
# car-main.py
#
# Modifying attributes of a class instance.
# New Car class that stores make, model, and year.
class Car():
    """A simple attempt to represent a car"""

    # odometer_reading is an attribute that will change over time
    def __init__(self, make, model, year):
        """Initialize attributes to car instance"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # Also extend function capability to ensure a value lower than the current
    # odometer_reading is not entered.  This prevents 'rolling back' the odometer_reading
    def update_odometer(self, mileage):
        """Sets odometer_reading to the provided value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer reading!")

    def increment_odometer(self, miles):
        """Add miles to the current odometer reading"""
        self.odometer_reading += miles





my_new_car = Car('chevy', 'silverado', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print(" ")

# Can modify an attribute directly through an instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print(" ")

# Can modify an attribute using a method
my_new_car.update_odometer(46)
my_new_car.read_odometer()
print(" ")

# This call prints the error message in update_odometer()
my_new_car.update_odometer(21)

# Can increment an attribute through a method
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.increment_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
