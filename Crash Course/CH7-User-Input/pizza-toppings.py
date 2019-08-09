# CH7 Exercise 7-4
#
# pizza-toppings.py
#
# Create loop to prompt user for pizza toppings
# until 'quit' is entered.
#
# Create prompt
prompt = "\nEnter a topping for your pizza: "
prompt += "\nType 'quit' to stop.  "

# Loop through input while topping is not 'quit'
while True:
    topping = input(prompt)

    # Check if 'quit' is entered
    if topping == 'quit':
        break
    else:
        print("\n" + topping.title() + " sounds delicious!")
