#METHOD OVERLOADING
# same class & same function or method name& differrnet parrameters

class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c

object=A()
print(object.sum(1,2,5))
