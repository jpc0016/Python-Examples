# CH8 Example
#
# printing_models.py
#
# Modifying lists in functions.
# Write two functions.  One handles printing the designs.  One handles
# summarize the prints made

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Show all models that were printed
    """
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

# Initialize lists
unprinted_designs = ['iphone cases', 'robot pendant', 'dodecahedron']
completed_models = []

# [:] notation sends a copy of unprinted_designs to prevent losing the list
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
