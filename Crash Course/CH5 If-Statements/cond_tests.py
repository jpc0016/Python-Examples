# CH5 Exercise 5-1 and 5-2: Conditional Tests
#
# Write a couple of Conditional tests and print results
#topping = 'sour cream'
#print("Is the topping tomatos?  I predict False.")
#print(topping == 'tomatos')

#print("\nIs the topping sour cream?  I predict True.")
#print(topping == 'sour cream')

#new_topping = 'lettuce'
#print("\nIs the next topping lettuce?  I predict True.")
#print(new_topping == 'lettuce')

#print("\nIs the next topping shredded cheese?  I predict False.")
#print(new_topping == 'shredded cheese')


###################################
###### Exercise 10-2 ##############
####### more conditionals #########
###################################
topping_list = ['sour cream', 'cheese', 'lettuce']
all_toppings = ['sour cream', 'veggies', 'cheese', 'beans', 'tomatos', 'lettuce', 'pico']

# loop through all toppings to see which toppings are selected
for topping in all_toppings:
    if topping in topping_list:
        print("I put " + topping + " in my burrito.")
    else:
        print("I don't like " + topping + ".")
