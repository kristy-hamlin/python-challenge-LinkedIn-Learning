# Python Essential Training Chapter 11
# Command Line Arguments

# To run a Python program from the terminal, all you do is navigate to the
# directory where the script is, then run the command "python <filename.py>".
# Some programs, including Python programs, can accept what are called 
# "Command line arguments". Usually, they are indicated by a - character followed by
# one letter that stands for something, or two -- characters followed by word.
# For example, -h vs -help.

# If you want to create a script that accepts command line arguments, there are different
# modules in Python that will help you do this. Today we will use the ArgumentParser class
# from the argparse module.
from argparse import ArgumentParser

# To allow your script to accept and use command line arguments, create an ArgumentParser
# object to create and setup arguments:
parser = ArgumentParser()

# The add_argument() function allows you to add an argument for your program to accpet.
# There are some keyword arguments you can use with this function, such as required=True
# to make the command line argument required. Another useful keyword argument is help='message',
# which you can use to provide a message explaining what the command line argument does. 
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program.')
parser.add_argument('--text', '-t', required=True, help='Text to write to the destination file.')
# NOTE: The argument '-help' or '-h' will be included without you programming it in. 
#       if the user calls this commandline argument, the program will print a list of all
#       the command line arguments possible along with the help message for each. 

# To use the arguments, you need to call the .parse_args() method, which will return a new
# type of object that stores the arguments as attributes:
args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text + '\n')

print(f'Wrote "{args.text}" to output file "{args.output}"')