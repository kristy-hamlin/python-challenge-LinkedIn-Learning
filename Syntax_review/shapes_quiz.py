# Python Essential Training: Chapter 7
# Drawing Shapes Challenge

# You are provided with a base Shape class, and a Square class which extends it. 
# You can see how the Square class works by modifying the test code. 
# The output of mySquare.print() is an ASCII art square.

# Fill in the Triangle class to print a triangle to the console. Can you print
# a right triangle? What about an equilateral (ish) triangle? Try to modify the 
# height and width of your triangle as well. Feel free to change how the base class
# is called. 

import math

class Shape:
    printChar = '#'

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def __init__(self, s):
        super().__init__(s, s)

    def printRow(self, i):
        print((self.printChar + ' ') * self.width)
		
def squareDemo():
    mySquare = Square(5)
    mySquare.print()

class Triangle(Shape):
    def __init__(self, h):
        super().__init__(2 * h, h)

    def printRow(self, i):
        # Width of any row i:
        rowWidth = i * 2 + 1
        padding = int((self.width - rowWidth)/ 2)
        print(' ' * padding + self.printChar * rowWidth)

def triangleDemo():
    myTriangle = Triangle(5)
    myTriangle.print()

triangleDemo()

# NOTE: I am ashamed to say this but I could not figure out how to get the triangle
# nice and lined up by myself. I need to keep practicing my problem solving skills
# and programming skills. 