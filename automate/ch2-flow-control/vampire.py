# CH2 Example
#
# vampire.py
#
# using multiple elif statements; page 41

# initialize variables
name = input('What is your name?\n')
age = 1000

# begin conditionals
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')
