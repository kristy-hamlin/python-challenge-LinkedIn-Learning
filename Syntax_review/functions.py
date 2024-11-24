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
def lamdaDemo(num):
    print(num)
    newNum = (lambda x: x * 2)(num)
    print(newNum)

lamdaDemo(5)
