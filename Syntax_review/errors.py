# Python Essential Training: Chapter 8

# If you have some code that may throw an error, you can use a try/except
# clause like so, that will catch the exception and stop execution from halting:
import time

def causeError():
    try:
        return 1/0
    except Exception as e:
        print(type(e))
        return e


# You can add a finally clause that will ALWAYS execute regardless of what happens
# in the try clause. Even if you don't include an except clause and an error is thrown
# and not caught, the finally clause will still execute:
def causeError2():
    try:
        return 1/0
    except Exception as e:
        print(type(e))
        return e
    finally:
        print('This executes 100% of the time!')

# One fun usecase for finally clauses is timing the execution of a function like so.
# You must import the time class to do this:
def causeError3():
    start = time.time() # current time in seconds
    try:
        time.sleep(0.5) # halts execution for n seconds
        return 1/0
    except Exception as e:
        print(type(e))
        return e
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

# You can have multiple except clauses to handle different types of exceptions.
# Python will check each exception type in order, so the order does matter.
# The first exception type that matches will cause that code to execute.
def causeError4(name='zero division'):
    try:
        if name == 'zero division':
            return 1/0
        elif name == 'type error':
            return 1 + 'a'
        else:
            print('Choose zero division or type error')
            return
    except TypeError:
        print('There was a Type Error')
    except ZeroDivisionError:
        print('There was a zero division error')
    except Exception:
        print('There was some type of exception')

# Notice that if we were to put the except Exception clause first, the
# most general one, the other two would never execute, because that is the 
# parent class of both of them and will always match:
def causeError5(name='zero division'):
    try:
        if name == 'zero division':
            return 1/0
        elif name == 'type error':
            return 1 + 'a'
        else:
            print('Choose zero division or type error')
            return
    except Exception:
        print('There was some type of exception')
    except TypeError:
        print('There was a Type Error')
    except ZeroDivisionError:
        print('There was a zero division error')

# Wrapper Functions --------------------------------------------------------
# You can imagine that we may have programs where we are constantly 
# checking for the same types of errors. Luckily, we can use a wrapper
# function to do this.
# The wrapper function accepts a function as an argument and returns the
# wrapper like so:

def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was a Type Error')
        except ZeroDivisionError:
            print('There was a Zero Division Error')
        except Exception:
            print('There was some sort of Exception')
    return wrapper

# Now, we use the handleException function as a decorator for other functions,
# and those checks that we created will happen:
@handleException
def causeError6():
    return 1/0

# But what if we want to use this decorator on a function that requires arguments?
# Well, we need to modify to accept some number of arguments using *args, as we
# saw previously:
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a Type Error')
        except ZeroDivisionError:
            print('There was a Zero Division Error')
        except Exception:
            print('There was some sort of Exception')
    return wrapper

# With this minor adjustment, we can now use this wrapper on functions that require
# arguments:
@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

# Custom Exceptions ---------------------------------------------------------
# Oftentimes, you will need to create your own exception classes that extend
# the base exception class. They key information is often in the name of that
# exception class and where you raise it in your code. 
class CustomException(Exception):
    pass

# Then, if you reach a point in your code where you want to raise that 
# exception, you can raise it like so. You can also pass in a message
# when calling it that will appear in the stack trace:
def causeError():
    raise CustomException('You called the causeError() function.')



class HTTPException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message: {self.message}')

class ServerNotFound(HTTPException):
    statusCode = 404
    message = 'Resource not found'

def raiseServerError():
    raise ServerNotFound()

raiseServerError()
