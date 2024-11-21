# Python Essential Training Chapter 2 Challenge:
# Write a function called factorial() that returns the factorial of the number passed in.
# If an input is not a positive integer or 0, you should return none. 

def factorial(x):
    #Confirm integer:
    if not isinstance(x, int):
        print('Input must be an integer.')
        return None
    #Confirm is non-negative:
    if x < 0:
        print('Input must be 0 or positive.')
        return None
    #Factorial:
    if x > 1:
        return x * factorial(x - 1)
    else:
        return 1

print('~~~~~~~~~~ Testing factorial - using recursion ~~~~~~~~~~ ')   
print('Factorial of 10 = ' + str(factorial(10)))
print('Factorial of 3 = ' + str(factorial(3)))
print('Factorial of 4 = ' + str(factorial(4)))
print('Factorial of -1 = ' + str(factorial(-1)))
print('Factorial of hello = ' + str(factorial('hello')))
print() #for output readability


def factorial2(x):
    #non recursive factorial
    #Confirm integer:
    if not isinstance(x, int):
        print('Input must be an integer.')
        return None
    #Confirm is non-negative:
    if x < 0:
        print('Input must be 0 or positive.')
        return None
    #Factorial Calculation:
    result = 1
    while x > 0:
        result = x * result
        x = x - 1
    return result

print('~~~~~~~~~ Testing factorial2 - non recursive ~~~~~~~~~~~')
print('Factorial of 3 = ' + str(factorial2(3)))
print('Factorial of 4 = ' + str(factorial2(4)))
print('Factorial of -10 = ' + str(factorial2(-10)))