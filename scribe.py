import time
import os
import math

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        #I think floating point errors is causing this to fail, 
        #So I am adding a rounding step here. 
        rounded_x = round(point[0])
        rounded_y = round(point[1])
        return rounded_x < 0 or rounded_x >= self._x or rounded_y < 0 or rounded_y >= self._y

    def setPos(self, pos, mark):
        x_rounded = round(pos[0])
        y_rounded = round(pos[1])
        self._canvas[x_rounded][y_rounded] = mark

    def print(self):
        self.clear()
        for y in range(self._y):
            print([' '.join([col[y] for col in self._canvas])])
        time.sleep(0.1)
   
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class TerminalScribe:
    def __init__(self, canvas, direction=180):
        self.direction = direction
        self.canvas = canvas
        self.pos = [0, 0]
        self.mark = '*'
        self.trail = '.'

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
    
    def forward(self, magnitude):
        dx, dy = self.getVector()
        i = 0
        while i < magnitude:
            newPos = [self.pos[0] + dx, self.pos[1] + dy]
            #print(f'pos = {self.pos}')
            #print(f'newPos = {newPos}')
            if not self.canvas.hitsWall(newPos):
                #print('Calling self.draw(newPos)')
                self.draw(newPos)
            i = i + 1

    def getVector(self):
        #Should work for all 4 Quadrants:
        #print(f'self.direction = {self.direction}')
        dx = (math.sin((self.direction/180) * math.pi))
        #print(f'dx = {dx}')
        #Since down on the Canvas means increasing y value, we multiply
        #the dy result by -1. 
        dy = (math.cos((self.direction/180) * math.pi)) * -1
        #print(f'dy = {dy}')
        return (dx, dy)

    def setDirection(self, direction):
        self.direction = direction

    #~~~~~~~~~ DIRECTIONS: ~~~~~~~~~~~~~~~~~~~~~~~~
    def up(self):
        pos = [self.pos[0], self.pos[1] - 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    
    def down(self):
        pos = [self.pos[0], self.pos[1] + 1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0] + 1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0] -1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    
    def move(self, vector):
        if (not isinstance(vector, tuple)):
            print('argument must be a tuple with 2 ints.')
            return
        else:
            if len(vector) != 2:
                print('argument must be a tuple of 2 ints.')
                return
        x, y = vector
        pos = [self.pos[0] + x, self.pos[1] - y]
        # NOTE: This function takes a positive y value to mean up.
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    
    #~~~~~~~~~ SHAPES: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def drawSquare(self, size):
        for i in range(0, size):
            self.right()
        for i in range(0, size):
            self.down()
        for i in range(0, size):
            self.left()
        for i in range(0, size):
            self.up()
    
    def drawTriangle(self, base):
        for i in range(0, base):
            self.move((2, 0))
        for i in range(0, base):
            self.move((-1, -1))
        for i in range(0, base):
            self.move((-1, 1))

    def drawEquilateralTriangle(self, base):
        pass
        # This was not working.

    def drawSurprise(self, size):
        for i in range(0, size):
            self.move((0, -i))
