from scribe import Canvas
from scribe import TerminalScribe

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

scribe.setDirection(90)
scribe.forward(5)
scribe.setDirection(135)
scribe.forward(6)
scribe.setDirection(180)
scribe.forward(4)
scribe.setDirection(225)
scribe.forward(4.5)
print(str(scribe.pos))