#!/home/Python/basic.py
# Very basic script to test functions in Python 3.7

def sum(number_one, number_two):
    
    number_one_int = convert_integer(number_one)
    number_two_int = convert_integer(number_two)
    
    result = number_one_int + number_two_int
    return result


def convert_integer(number_string):

    new_integer = int(number_string)
    return new_integer

answer = sum(1, 3)
print(answer)
