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
# We rely on the fact that threads share memory. 