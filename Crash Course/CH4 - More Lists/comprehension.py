# CH4 List comprehension exercises 4-3 to 4-9
#
# print numbers 1-20 in a for loop
# print([number for number in range(1,21)])

# Create list of numbers from 1 to 1,000,000.  Verify list using
# min(), max(), and sum()
# list = []
# for i in range(1,1000001):
#     list.append(i)

# print(min(list))
# print(max(list))
# print(sum(list))

# use third argument in range() to make a list of odd numbers from 1 to 20
# change to 1 - 33 every third number
# numbers = []
# for number in range(3,34,3):
#     numbers.append(number)
#     print(number)

# make a list of 10 cubes (n ** 3) in the range 1 - 10
# cubes = []
# for i in range(1,11):
#     cubes.append(i**3)
#     print(i**3)

# change above loop to list comprehension
cubes = [i**3 for i in range(1,11)]
print(cubes)
