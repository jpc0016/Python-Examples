# CH7 Example
#
# greeter.py
#
# Using input() function
# Prints a prompt to the user like: "Please enter your username: "
# name = input("Please enter your name: ")
# print("Hello " + name.title() + "!")

# Can store the prompt as a variable and pass it to input()
prompt = "If you tell us who you are, we can personalize your message.  "
prompt += "\nWho are you?  "

name = input(prompt)
print("Hello " + name.title() + "!")

age = input("How old are you?  ")
age = int(age)
print(age)

if age >= 18:
    print("You can vote.")
