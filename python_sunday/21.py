class p1:
    def show(self):
        print("show from p1")
    def showusers(self):
        print("showusers from p1")   

class p2(p1):
    def showposts(self):
        print("showposts from p2")

objp2 = p2()
objp2.showposts()
objp2.show()
objp2.showusers()                