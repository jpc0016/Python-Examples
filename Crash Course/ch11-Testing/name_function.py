# CH11 Example
#
# name_function.py
#
# Simple function to troubleshoot
# Make middle name optional for test case to pass
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted first and last name"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
