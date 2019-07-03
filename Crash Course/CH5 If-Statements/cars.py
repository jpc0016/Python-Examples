# CH5 If-statements
#
# cars.py example
#

cars = ['audi', 'bmw', 'subaru', 'toyota']

# Simple if-statement inside a for loop
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
