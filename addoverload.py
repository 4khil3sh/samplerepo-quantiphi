
import math
 
class Square:
 
    def __init__(self, side):
        self.__side = side
 
    def setSide(self, side):
        self.__side = side
 
    def getSide(self):
        return self.__side
 
    def area(self):
        return self.__side ** 2
 
    def __add__(self, another_square):
        return Square( self.__side + another_square.__side )
 
c1 = Square(4)
print(c1.getSide())
 
c2 = Square(5)
print(c2.getSide())
 
c3 = c1 + c2
print(c3.getSide())