# CH5 Exercise 8-14
#
# cars-2.py
#
# Write a function that stores info about a car in a dictionary.  Function will always
# receive manufacturer and model name.  It will then accept an arbitrary number of
# inputs after
def create_car(make, model, **specs):

    # Create empty car dictionary
    new_car = {}

    # First two attributes are always provided
    new_car['make'] = make
    new_car['model'] = model

    # Loop through remaining attributes using key, value, .items()
    for key, value in specs.items():
        new_car[key] = value

    return new_car

# Call function with example provided by problem 8-14
car = create_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
