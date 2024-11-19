import math

class Area:
    def circle(self,r):
        print(math.pi * r**2)

    def square(self,side):
        print(side**2)    

areaobj = Area()

areaobj.circle(8)
areaobj.square(10)
