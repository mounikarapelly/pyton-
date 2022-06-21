class A:
    def display(self):
        print("thi s is  class a")

class B(A):
     def display(self):
         print("this is class B")
         super().display()

obj=B()
obj.display()