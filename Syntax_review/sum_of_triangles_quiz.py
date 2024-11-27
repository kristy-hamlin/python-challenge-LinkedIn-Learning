# Python Essential Training: 

# You are given a function triangle() that returns the triangular number
# for a given input, num. Your goal is to use this to create a function called
# square() that returns the square of a positive integer, num. 

# A triangular number is a number plus all the numbers less than itself.
# triangle(3) = 3 + 2 + 1 = 6

# Fill in the function square() that returns the square of a number using only the 
# triangle function. No multiplication or exponents allowed.

# I will also implement triangle(num) just as a bonus without looking:

def triangle(num):
    if num == 1:
        return 1
    else:
        return num + triangle(num - 1)

def square(num):
    if num > 1:
        return (triangle(num) + triangle(num - 1))
    elif num == 1:
        return 1
    else:
        print('Invalid input')
        return 0

print('2^2 = ' + str(square(2)))
print('3^2 = ' + str(square(3)))
print('4^2 = ' + str(square(4)))
print('5^2 = ' + str(square(5)))
print('6^2 = ' + str(square(6)))