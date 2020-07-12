#!/usr/bin/python3

# Sith name creator
import os
import random

first = ["Darth"]
first.append("General")
first.append("Count")

# Create 10 names
for i in range(0,9):
    last = os.popen('curl -d "gender=N&choice=1&displaypref=noprint&submit=Generate%21" -s https://www.dimfuture.net/starwars/random/generate.php | grep button.gif | cut -d ";" -f 3 | cut -d "<" -f 1 | tr -d "\n"').read()
    rand = random.random()

    if rand < 0.33:
        print(first[0] + " " + last)
    elif rand >= 0.33 and rand < 0.66:
        print(first[1] + " " + last)
    else:
        print(first[2] + " " + last)

print("\n")
