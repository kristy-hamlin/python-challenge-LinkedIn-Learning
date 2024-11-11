from scribe import *

canvas = Canvas(30, 20)
scribe = TerminalScribe(canvas, 180)

#Each letter is 5 x 5?

#Letter H
scribe.move((1,0))
scribe.forward(5)
scribe.move((0, 3))
scribe.setDirection(90)
scribe.forward(4)
scribe.move((0,2))
scribe.setDirection(180)
scribe.forward(5)


#Letter I
scribe.move((2, 5))
scribe.setDirection(180)
scribe.forward(5)

#Letter R
scribe.move((2, 5))
scribe.setDirection(180)
scribe.forward(5)
scribe.move((0,5))
scribe.setDirection(90)
scribe.forward(3)
scribe.setDirection(180)
scribe.forward(2)
scribe.setDirection(270)
scribe.forward(3)
scribe.setDirection(135)
scribe.forward(4)

#Letter E
scribe.move((2, 5))
scribe.setDirection(180)
scribe.forward(5)
scribe.move((0, 5))
scribe.setDirection(90)
scribe.forward(4)
scribe.move((-4, -2))
scribe.forward(4)
scribe.move((-4, -3))
scribe.forward(4)

#Letter K
scribe.move((-15, -5))
scribe.setDirection(180)
scribe.forward(7)
scribe.move((5, 7))
scribe.setDirection(225)
scribe.forward(5)
scribe.setDirection(135)
scribe.forward(5)