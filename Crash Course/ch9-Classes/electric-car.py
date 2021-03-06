# CH9 Example
#
# electric-car.py
#
# Demonstration of a child class.  A child class inherits attributes from the
# parent class.  The parent class must be within the same file as the child
# class and appear before it.
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

        # Initialize attributes specific to ElectricCar
        self.battery_size = 70

    def describe_battery(self):
        """Print statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # This method overrides the one in the parent class because it has the same
    # name.  Python will ignore Car.fill_gas_tank() and run this method instead.
    def fill_gas_tank(self):
        """Electric vehicles don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# Create a Tesla
tesla = ElectricCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())

# Test new ElectricCar method
tesla.describe_battery()
tesla.fill_gas_tank()
