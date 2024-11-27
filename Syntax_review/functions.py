# Python Essential Training Chapter 6

# Positional arguments are the "normal" way of providing arguments.
# When you call the function, which value gets assigned to which variable
# is based on the position:
def noKeywordArgumentsDemo(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'mul' or operation == 'multiply':
        return num1 * num2


# Keyword Arguments:
# In the function def, provide the arg name and the default value.
# Keyword arguments must come after positional arguments in the signature.
# When calling the function, keyword arguments can be provided in any order
# as long as the name is given.
# If no name is given, it will assume the order is the same as the signature.
def keywordArgumentsDemo(num1, num2, operation='sum', msg = 'default message'):
    print('msg = ' + msg)
    print('operation = ' + operation)
    if operation == 'sum':
        return num1 + num2
    if operation == 'mul' or 'multiply':
        return num1 * num2

# *args: 
# Using *args allows you to pass in a variable number of positional arguments:
# *args is a tuple.
def argsDemo(*args):
    print(args)
    print(type(args))

# **kwargs:
# **kwargs allows you to pass in a variable number of keyword arguments.
# **kwargs is a dictionary. 
# You do not have to use *args to use **kwargs, but you can use them
# together. 
def kwargsDemo(**kwargs):
    print(kwargs)
    print(type(kwargs))

# Local and Global Variable Scope in Python:
# Functions have access to variables that are defined in the main code.
# If there is a local variable that has the same name as a global variable,
# the local variable value will be used. 
# Functions do not have access to each other's local variables. 
globalMessage = 'global string'
varA = 10
def localVariablesDemo(varA, varB, varC):
    print(varA)
    print(varB)
    print(varC)
    print(globalMessage)

# Functions are Variables:
# In Python, you create a list of functions and iterate over them
# like so:
text = """
About three things I was absolutely positive.
First, Edward was a vampire.
Second, there was a part of him - and I didn’t know how dominant that part might be - that thirsted for my blood.
And third, I was unconditionally and irrevocably in love with him.
"""
def removeNewLines(text):
    return text.replace('\n', ' ')

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.', '-', ',', '*', '(', ')']
    for punc in punctuations:
        text = text.replace(punc, ' ')
    return text

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) < 8])

# Now, we can create a list of functions and iterate over it like so:
def listOfFunctionsDemo():
    print(text)
    processingFunctions = [removeNewLines, lowercase, removePunctuation, removeLongWords]
    for func in processingFunctions:
        text = func(text)
    print(text)

# Lambda Functions:
# Lambda Functions are one-line functions defined using the keyword lamda.
# They have many use cases for when you need a short function that does not
# need to get called again.
def lambdaDemo(num):
    print(num)
    newNum = (lambda x: x * 2)(num)
    print(newNum)

def lambdaDemo2(num1, num2):
    # You CAN name a lambda function and then call it like a regular function
    # by saving the function in a variable name:
    lambda_add = lambda x, y: x + y
    print(lambda_add(num1, num2))

# The first use case of the lambda function we will look at is to provide a function
# as an argument to the map() function. The map() function accepts a function
# and an iterable, and applies that function to every member of the iterable. 
def lambdaUseCaseMapping(method = 'lambda'):
    nums = list(range(0, 11))
    print('Nums Before Mapping: ' + str(nums))
    print('Method = ' + method)

    if method == 'normal':
        def square(x):
            return x**2
        squares = list(map(square, nums))
    elif method == 'lambda':
        squares = list(map(lambda x: x**2, nums))
    else:
        print('Choose "lambda" or "normal" for method.')
        return
    
    print('Nums after mapping: ' + str(squares))

# The second use case we will look at for lambda functions is used with the filter()
# function. The filter() function accepts a function that returns true or false, along 
# with an iterable. Then, it keeps items that return True, and does NOT keep items that
# return False. 
# The filter function returns a filter object, so remember to cast it to a list if that
# is what you want. 
def lambdaUseCaseFilter():
    nums = list(range(0, 21))
    print('nums: ' + str(nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print('evens: ' + str(evens))


# The third use case we will look at for lambda functions is as the key value
# for the sorted() function. The sorted() function sorts a list. However,
# in some cases, you may want it to sort by some feature other than the default. 
# You can provide a lambda function as the "key" keyword argument to the sorted()
# function and it will sort by that function. Let's take a look:
def lambdaUseCaseSorted():
    # By default, Sorted() will sort a list of words based on alphabetical
    # order:
    words = ['hello', 'goodbye', 'happiness', 'family']
    print('Unsorted: ' + str(words))
    words = sorted(words)
    print('Sorted: ' + str(words))

lambdaUseCaseSorted()

def lambdaUseCaseSorted2():
    # But we can use a lambda function and the key keyword parameter
    # to have it sort based on a different feature.
    words = ['Halloween', 'Christmas', 'New Years', 'Valentines', 'St Patrick', 'Veterans Day', 'Independence Day']
    print('Unsorted: ' + str(words))
    words = sorted(words, key=lambda x: len(x))
    print('Sorted: ' + str(words))

def lambdaUseCaseSorted3():
    # Let's look at another example where we sort a list of tuples.
    # We will use a lambda function to tell sorted() which element
    # in each tuple to use as the key.
    listOfTuples = [(3, 'b', 'hamster'), (1, 'c', 'cat'), (2, 'a', 'dog')]
    print('Unsorted: ' + str(listOfTuples))
    listOfTuples = sorted(listOfTuples, key=lambda x: x[1])
    print('Sorted: ' + str(listOfTuples))

lambdaUseCaseSorted3()