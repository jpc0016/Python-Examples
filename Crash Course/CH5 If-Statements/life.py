# CH5 Exercise 5-6
#
# Stages of life
# Write an if-elif-else statement that determines a person's stage in life

# Create a value for the age variable
# no need to declare age as 'int'
age = 64

# Remember the statement exits upon first condition met.  Simple elif-statements
# for the upper age limit are adequate
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")
