import turtle as tt
from settings import Segments, Numbers, Colon
import time, asyncio

tt.speed(2)
class DigitalClock:
    def __init__(self):
        self._Numbers = Numbers
        self._Segments = Segments
        self._Colon = Colon
        tt.speed('slow')
        tt.hideturtle()
        tt.penup()

    def __getAbsolutePositions(self, begin, reletivePositons):
        return [point for point in map(
            lambda p:(p[0]+begin[0], p[1]+begin[1]), reletivePositons)]

    def __drawSeg(self, seg, beginPos: tuple):
        """draw one segment of the digit
        param seg: which segment in a digital '8' to draw
        param topleft:a tuple: (x，y)
        """

        # calculate absolute position
        absolutePositions = self.__getAbsolutePositions(beginPos, self._Segments[seg])

        tt.goto(absolutePositions[0])
        tt.pendown()
        tt.begin_fill()
        for point in absolutePositions:
            tt.goto(point)
        tt.end_fill()
        tt.penup()


    def __drawDigit(self, number, beginPos: tuple):
        if number < 0 or number > 9:
            # invalid number  
            exit(1)

        number = self._Numbers[number]
        for seg in range(len(number)):
            if number[seg] == 1:
                self.__drawSeg(seg, beginPos)
    
    def __drawColon(self, beginPos: tuple):
        for i in range(2):
            absolutePositions = self.__getAbsolutePositions(beginPos, self._Colon[i])
            tt.goto(absolutePositions[0])
            tt.pendown()
            tt.begin_fill()
            for point in absolutePositions[1:]:
                tt.goto(point)
            tt.end_fill()
            tt.penup()


    def displayTime(self):
        now = time.strftime("%H:%M", time.localtime()).split(':')
        # draw hour
        tt.color('#298FEF')
        self.__drawDigit(int(now[0][0]), (-42 * 2, 0))
        self.__drawDigit(int(now[0][1]), (-42 * 1, 0))
        tt.color('#b2cf87')
        self.__drawColon((0, 0))
        tt.color('#298FEF')
        self.__drawDigit(int(now[1][0]), (10, 0))
        self.__drawDigit(int(now[1][0]), (50, 0))

async def displayClock():
    clock = DigitalClock()
    # loop = asyncio.get_running_loop()
    # end_time = loop.time() + 60.0 * 10 # 10 mins
    while True:
        clock.displayTime()
        # if(loop.time() + 1.0) >= end_time:
        #     break
        tt.clear()
        await asyncio.sleep(8)

if __name__ == '__main__':
    asyncio.run(displayClock())
