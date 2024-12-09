# This file is a module because it contains functions that you can use when you import
# it into another python script.

def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes