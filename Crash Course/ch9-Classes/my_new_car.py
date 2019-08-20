# CH9 Example
#
# my_new_car.py
#
# Importing a class from a separate file.

from car import Car

my_new_car = Car('chevy', 'silverado', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print(" ")

# Can modify an attribute directly through an instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print(" ")
