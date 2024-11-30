# Python Essential Training Chapter 8 Challenge: Bad Arguments

# Fill in a custom annotation called handleNonIntArguments that
# raises a custom exception called NonIntArgumentException if any
# of the arguments passed to a function are not integers. 

# More Precisely:
# Create a custom exception called NonIntArgumentException.
# Fill in the wrapper function in the handleNonIntArguments function
# to act as an annotation.
# Check the test code to make sure you understand how this annotation
# is being used. 

class NonIntArgumentException(Exception):
    def __init__(self, x):
        super().__init__(f'NonIntArgumentException: Non integer argument detected: {x}')

def handleNonIntArguments(func):
    def wrapper(*args):
        for var in args:
            if not isinstance(var, int):
                raise NonIntArgumentException(var)
        return func(*args)
    return wrapper

@handleNonIntArguments
def int_sum(*args):
    total = 0
    for a in args:
        total = total + a
    return total

x = int_sum(1, 2, 3, 4, 5, 6, 'hello')
print(x)

# Seems to be working! 
# Note: The wrapper function needs to return func(*args), otherwise
# it returns none and using the decorator won't work. 
