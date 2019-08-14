# Chapter 3 Exercises 3-1, 3-2, & 3-3
#
# Create a list of names and print each element

names = ['Jeff', 'Peter', 'Quindarius', 'Carlos', 'Zhang']

i = 0
for str in names:
    print("Hi " + names[i] + "!")
    i += 1

transpo = ['car', 'boat', 'plane', 'douche canoe']

j = 0
for element in transpo:
    print("I would love to own a " + transpo[j])
    j += 1

# Same as above but with list comprehension
[print("I would love to own a " + transpo[j]) for j in range(4)]
