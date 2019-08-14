# CH5 Exercise 5-11
#
# ordinal numbers
#
# Print proper ordinal ending for each number 1 - 9 using an if-elif-else statement
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
