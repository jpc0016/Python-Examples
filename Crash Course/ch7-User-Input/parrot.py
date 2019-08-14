# CH7 Example
#
# parrot.py
#
# Flag introduction
# Use a flag to determine whether the program should continue running
prompt = "Tell me something and I will repeat it back to you:  "
prompt += "\nEnter 'quit' to end the program.  "

# Set initial state to true
active = True
while active:
    message = input(prompt)

    # Check if 'quit' was entered.  If not, go ahead and repeat message.
    if message == 'quit':
        active = False
    else:
        print("\n" + message + "\n")
