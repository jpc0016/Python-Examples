# CH8 Exercise 8-15
#
# print_models_example.py
#
# Import the functions originally in printing_models.py
# Functions are in printing_functions.py
import printing_functions

# Initialize lists
unprinted_designs = ['iphone cases', 'robot pendant', 'dodecahedron']
completed_models = []

# [:] notation sends a copy of unprinted_designs to prevent losing the list
printing_functions.print_models(unprinted_designs[:], completed_models)
printing_functions.show_completed_models(completed_models)
