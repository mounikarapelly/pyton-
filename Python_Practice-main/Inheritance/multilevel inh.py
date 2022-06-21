class Main:
    def fun1(self):
        print("this is main class")

class sub(Main):
    def fun2(self):
        print("this sub class of main class")

class SuperSub(sub):
    def fun3(self):
        print("this is super sub class")

object=SuperSub()
object.fun1()
object.fun2()
object.fun3()