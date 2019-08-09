# CH7 Example
#
# cities-2.py
#
# Intro to Break.
# Continuously prompt user for a city.  Break loop when "quit"
# is entered.
prompt = "\nPlease enter the name of a city you have visited:  "
prompt += "\nEnter 'quit' to end the program.  "

# Loop always.  Break later.
while True:
    message = input(prompt)

    # Check if 'quit' was entered.  If not, go ahead and repeat message.
    if message == 'quit':
        break
    else:
        print("\nI'd love to go to " + message.title() + "!")
