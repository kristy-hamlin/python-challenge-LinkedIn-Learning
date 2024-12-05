# Python Essential Training: Chapter 10
# Working with Files:


# ----------------READING FILES ----------------------------

def readingDemo1():
    # The open() function is used to open a file. The first positional argument is
    # the relative path to the file, the second argument in this case is a string, 'r',
    # which signifies we will be only reading the file, not writing it:
    f = open('Holiday_glow.txt', 'r')
    print(f)
    # This should print the f object, which is a file object.
    # Make sure that the CWD (current working directory) in VSC is the directory
    # where this script is, otherwise it will look for the file relative to whatever
    # the CWD, not where the python script is. 

def readingDemo2():
    # Once you open a file, you can get one line at a time using the .readline()
    # function:
    f = open('Holiday_glow.txt', 'r')
    print(f.readline())
    # The readline() function returns one line at a time and automatically moves
    # to the next line whenever called.

def readingDemo3():
    # The readlines() function, note the S, plural - returns a list of strings of
    # all the unread lines in the file:
    f = open('Holiday_glow.txt', 'r')
    print(f.readlines()) # This prints the list of all the lines.

def readingDemo4():
    # To attractively print the poem, we can use the string processing function .strip(),
    # which will strip all the extra whitespace from each line including newlines.
    # If we print the list without using .strip(), we will have double spaces because print()
    # includes a newline, and it will also print each newline in the poem.
    f = open('Holiday_glow.txt', 'r')
    for line in f.readlines():
        print(line.strip())

# ---------------- WRITING FILES ----------------------------

def writingDemo1():
    # To open a file to write to, you pass in a 'w' instead of an 'r'.
    # If the file does not yet exist, it will be created. If it does 
    # exist, it will be overwritten with an empty file:
    f = open('output.txt', 'w')
    print(f)

    # The .write() function will write a line of text to the file:
    f.write('Merry Christmas\n') # we need to add our own newlines.
    f.write('and a Happy New Year!\n')

    # One thing to keep in mind is that writing to files happens via a 
    # buffer. That buffer does not get emptied every time f.write() is
    # called, but it does get emptied for sure when the file is closed.
    # This is one of many reasons that it is good practice to close
    # files:
    f.close()

def writingDemo2():
    # If you want to append to an existing file without starting from scratch,
    # use 'a' mode:
    f = open('output.txt', 'a')
    f.write('Let next year be even \n')
    f.write('more wonderful than this year\n')
    f.write('and full of new adventures.\n')
    f.close()

def writingDemo3():
    # Making sure to close the file is so important that the proper way to 
    # open files is actually a syntax that will automatically close the files.
    # That syntax is the "with open" syntax. As soon as that block is done,
    # you still have access to the file object to see its attributes, but the file
    # is closed and you cannot write to it anymore:
    with open('output.txt', 'a') as f:
        f.write('\n')
        f.write('2025 will be a time of growing\n')
        f.write('and a time of joy and happiness!\n')
    print(f)

writingDemo3()

# End of reading/writing text files lesson. 