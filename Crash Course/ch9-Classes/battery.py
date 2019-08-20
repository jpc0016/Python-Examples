# CH9 Example
#
# battery.py
#
# Demonstration of instances as attributes.  A growing list of attributes can be
# moved into a separate class and use it as an attribute to ElectricCar
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

    def fill_gas_tank(self):
        """Print statement about filling gas tank"""
        print("Filling gas now.")



# New Battery class that does not inherit from any class
class Battery():
    """Simple class to model the battery for an electric car"""

    def __init__(self, battery_size=70):
        """Initialize Battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # New method exclusive to Battery() class
    def get_range(self):
        """Prints a statement about range based on battery size"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."

        print(message)




# Pass parent class 'Car' into the child class.
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    # Still have an __init__() method in child class with same parameters as
    # parent class __init__()
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        # Special function that helps Python make connections between parent and
        # child class.  Super() comes from calling parent class a 'superclass' and
        # child class a 'subclass'.  Note: Python2.7 has slightly different
        # inheritance. Only difference is: super(ElectricCar, self).
        super().__init__(make, model, year)

        # Initialize battery attribute using the Battery class
        self.battery = Battery()



    # This method overrides the one in the parent class because it has the same
    # name.  Python will ignore Car.fill_gas_tank() and run this method instead.
    def fill_gas_tank(self):
        """Electric vehicles don't have gas tanks."""
        print("This car doesn't need a gas tank!")




# Create a Tesla
tesla = ElectricCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())

# Test Battery attribute
tesla.battery.describe_battery()
