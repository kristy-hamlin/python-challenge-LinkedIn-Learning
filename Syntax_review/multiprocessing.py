# Python Essential Training: Chapter 9
# Multiprocessing

# For this lesson we are going to use a third party module called multiprocess.
# The official Python module is used in the exact same way and is called multiprocessING.
# However, the official module does not allow you to start new processes calling functions
# that are defined in the same file.

from multiprocess import Process
import time

def longSquare(n, resultDict):
    time.sleep(1)
    resultDict[n] = n ** 2


    # Notice that using the multi-processes has basically the same syntax as
    # for threads. You need a target function, the arguments, you call .start(),
    # and you call .join(). What happens if we run this demo?
def multiprocessingDemo1():
    results = {}

    p1 = Process(target=longSquare, args=(1, results))
    p2 = Process(target=longSquare, args=(2, results))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(results)
    # Of course, the results dictionary prints empty in this case. Recall that
    # processes have their own memory space, so the baby processes cannot write
    # to the dictionary in the parent process. 

# When you create multiple processes, your computer literally uses multiple processes
# and runs them simultaneously. If we create more than a couple processes and print
# the results directly from the function so we can see them, you will start to see
# that the print statements are not coordinated:
def longSquare2(n):
    time.sleep(1)
    print(n**2)
    print('Finished Computing!')

def multiprocessingDemo2():
    processes = [Process(target=longSquare2, args=(n,)) for n in range(0,10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

#-----------------------Call functions below-------------------------
# For multiprocessing, we need to include the following line. This ensures
# that child processes don't create infinite baby processes because they are
# running the same main code, if I am understanding correctly. 
if __name__ == '__main__':
    multiprocessingDemo2()
