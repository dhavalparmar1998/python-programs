import math

class Area:

    def __init__(self):
        self.pi=math.pi

    def circle(self,r):
        print(self.pi * r**2)

    def square(self,side):
        print(side**2)    

areaobj = Area()

areaobj.circle(8)
areaobj.square(10)
