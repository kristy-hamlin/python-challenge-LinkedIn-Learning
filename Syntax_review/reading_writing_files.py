# Python Essential Training: Chapter 10
# Working with Files:

def readingDemo1():
    # The open() function is used to open a file. The first positional argument is
    # the relative path to the file, the second argument in this case is a string, 'r',
    # which signifies we will be only reading the file, not writing it:
    f = open('Holiday_glow.txt', 'r')
    print(f)
    # This should print the f object, which is a file object.

readingDemo1()