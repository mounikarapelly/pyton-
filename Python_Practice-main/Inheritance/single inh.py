class Parent:
    def fun1(self):
        print("this is main class")

class Child(Parent):
     def fun2(self):
         print("this is sub class of parent class")

object=Child()
object.fun2()
object.fun1()