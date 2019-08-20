# CH9 Example
#
# my_cars.py
#
# Importing multiple classes from a separate file.

# can use "from car import *" as well
from car import Car, ElectricCar

# create new car: beetle
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

# create new electric car: tesla
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
