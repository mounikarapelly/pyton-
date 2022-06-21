class display:
    def fun1(self):
        print("this is display one")

class show(display):
    def fun2(self):
        print("this show function")

class view(display):
    def fun3(self):
        print("this is view")



object=view()
object.fun1()
#object.fun2()
object.fun3()