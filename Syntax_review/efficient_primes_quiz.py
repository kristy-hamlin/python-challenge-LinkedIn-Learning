# Chapter 5 Challenge: Efficient Primes
# Write a function called allPrimesUpTo() which returns a list of all primes
# up to the given input number.

# Input: num - a whole positive integer
# Output: list - a list of all integer primes less than num

# Make the function efficient by using the list of previously found primes
# to test for the current prime instead of testing all possible factors. 

def allPrimesUpTo(num):
    primes = [2]
    for x in range(2, num + 1):
        for prime in primes:
            if x % prime == 0:
                break
        else:
            primes.append(x)
    return primes


print(allPrimesUpTo(11))    
