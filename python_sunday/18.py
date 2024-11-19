class Area:
    def circle(self,r):
        print(22/7 * r**2)

    def square(self,side):
        print(side**2)    


areaobj = Area()

areaobj.circle(8)
areaobj.square(10)