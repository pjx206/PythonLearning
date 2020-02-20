import turtle as tt
from settings import Segments, Numbers

#! Turtle uses a normal cordinate system: (0, 0) is left bottom
#! points in segments is using a screen cordinate system: (0, 0) is left top

class DigitClock:
    def __init__(self, initTime):
        """initTime format: hh:mm:ss"""
        tmp = initTime.split(':')
        self._hour = tmp[0]
        self._minute = tmp[1]
        self._seconf = tmp[2]
        self._Numbers = Numbers
        self._Segments = Segments
        tt.isvisible = False

    def __drawSeg(self, seg, leftTop: tuple):
        """draw one segment of the digit
        param seg: which segment in a digital '8' to draw
        param topleft:a tuple: (x，y)
        """

        # calculate absolute position
        absolutePositions = [point for point in map(
            lambda p:(p[0]+leftTop[0], p[1]+leftTop[1]), self._Segments[seg])]

        tt.penup()
        tt.goto(absolutePositions[0])
        tt.pendown()
        tt.begin_fill()
        for point in absolutePositions:
            tt.goto(point)
        tt.end_fill()
        tt.penup()

    def DisplayDigit(self, number, leftTop):
        if number < 0 or number > 9:
            # invalid number
            exit(1)

        number = self._Number[number]
        for seg in range(len(number)):
            if number[seg] == 1:
                self.__drawSeg(seg, leftTop)
