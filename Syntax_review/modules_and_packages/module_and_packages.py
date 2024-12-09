# Python Essential Training Chapter 11
# Creating Modules and Packages

# There is no real formal definition of a library in Python. Generally, it tends to mean
# modules or packages that you import to use code (functions, classes, etc) that someone else
# wrote or that is organized in a different file from the script you are writing. 
#   module - a single Python file containing functions or classes that you import.
#   package - a folder containing multiple modules. Must contain a python file called '__init__.py'

# NOTE: It is convention to include all imports at the top of the code. However I will not 
#       follow this convention in this file so that the code for each example is together.

# ------------------------ MODULES --------------------------------
# To use a function from the module we created, primes.py, we need to import it and then 
# call the function using the module name:
import primes

print(primes.isPrime(5))

# You can import an individual function from a module using the following syntax.
# When you import an individual function, you do not need to use the file name
# when calling the function:
from primes import listPrimes

print(listPrimes(100))

# You can also give a different name to use for the module when importing it
# for clarity or convenience:
import primes as p

print(p.isPrime(100))

# ------------------ PACKAGES -------------------------------------
# Packages are directories which contain multiple related Python modules. 
# For these examples, we create a simple package called "numbers", which contains
# two modules. The primes2.py module, and the factors module. 
# To import a function from a package, you need to specify the package name and the module
# name with the following syntax: from <package>.<module> import <function>:
from numbers.factors import getFactors
print(getFactors(100))

# NOTE: modules in packages often reference one another. For modules in the same package,
#       you still need to use an import statement identical to the one in the previous
#       example. from <package>.<module> import <function>

# ---------------------- __NAME__ --------------------------------
# One last thing you should understand in Python is how the built-in variable __name__ works.
# The python script or file that you call from the terminal will be called __main__:
print(f'The name of "module_and_packages.py" is currently: "{__name__}"')

# When you import a module in Python, all of the code in the module is executed. Most of
# the time, you don't realize this because modules only contain function and class 
# definitions, and not code that has any output. For this demonstration, let's 
# see what those files call themselves when they are imported, not run directly. 

# Lastly, one common pattern in Python is to provide some text that will only run 
# if a file is directly called using the following pattern. Normally this is done inside
# modules, not a file that is intended to be directly run, but we will do it here
# so that you can see the pattern and understand the premise:
if __name__ == '__main__':
    print('This code will only run when this file is called directly, not imported.')