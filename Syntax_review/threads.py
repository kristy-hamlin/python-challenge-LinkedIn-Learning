# Python Essential Training: Chapter 9
# Threads and Processes

# Different processes do not have access to each other's short term memory. But
# different threads, contained within the same process, do. First, we will learn
# how to use threads in Python.

import threading
import time

def longSquare(num):
    time.sleep(1)
    return num**2

def longSquareDemo():
    squareList = [longSquare(n) for n in range(0, 5)]
    print(squareList)

# Here, we have contrived an example function that will take long to execute. 
# In the real world, you may have your program waiting on data form a server.
# To allow the program to accomplish work while it is waiting, we can use 
# multiple threads:
def threadsDemo1():
    # To create multiple threads, we use the threading.Thread function.
    # It requires two arguments, the target function, and any arguments.
    t1 = threading.Thread(target=longSquare, args=(1,)) # Args passed in as tuple.
    t2 = threading.Thread(target=longSquare, args=(2,)) # Trailing comma indicates 1 argument tuple. 

    t1.start()
    t2.start()

    # The .join() function waits to see if all the threads have completed
    # and joins the execution:
    t1.join()
    t2.join()

# But where are the results of these functions? Well, we need to do a trick to get them.
# We rely on the fact that threads share memory. We can create a results dictionary in the main
# program, and then edit our function so that it accepts a dictionary. Then both threads will
# be able to access and write to that dictionary. Like so:

def longSquare2(n, results):
    time.sleep(1)
    results[n] = n ** 2

resultDictionary = {}

def threadsDemo2():
    t1 = threading.Thread(target=longSquare2, args=(1, resultDictionary))
    t2 = threading.Thread(target=longSquare2, args=(2, resultDictionary))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# One common pattern is to create a list of threads, since often times we want a variable number
# of threads. Using the list datastructure will allow us to easily access all of those threads without
# having to individually create or name them:
def threadsDemo3():
    threads = [threading.Thread(target=longSquare2, args=(n, resultDictionary)) for n in range(0, 10)]
    [t.start() for t in threads]
    [t.join() for t in threads]

# Interestingly, chatgpt agrees with my confusion that the professor used a list comprehension
# to start and join the threads and assigned them to nothing. Chatgpt recommends using standard loops.
# I know this lady is the pro, so maybe chatgpt is wrong. But let's do it both ways for practice:

def threadsDemo4():
    threads = [threading.Thread(target=longSquare2, args=(n, resultDictionary)) for n in range(0, 20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

threadsDemo4()
print(resultDictionary)

# That's it for this brief intro to threads. 