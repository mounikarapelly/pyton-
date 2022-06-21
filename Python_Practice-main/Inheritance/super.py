class A:
    def __init__(self):
        print("this is main class")


    def fun1(self):
        print("this is function")

class B(A):
    def __init__(self):
        print("this is class b")
        super(B, self).__init__()
    def fun2(self):
        print("this is last class")
        

object=B()