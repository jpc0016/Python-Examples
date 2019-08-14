# CH8 Example
#
# making_pizzas.py
#
# Importing a module

# this module comes from pizza_module.py and only includes the function we want:
# make_pizza()
# Can also import specific functions: "from pizza_module import make_pizza"
import pizza_module

# Output is the exact same as in pizza-2.py
# dot notation is not required if importing specific functions from a module
pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'pineapple', 'sausage', 'anchovies')
