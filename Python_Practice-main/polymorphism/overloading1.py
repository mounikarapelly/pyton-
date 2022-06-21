class employee1():
    def name(self):
        print("Mounika patel is his name")
    def salary(self):
        print("20000 is his salary")
    def age(self):
        print("22 is his age")

class employee2():
    def name(self):
        print("srikanth is his name")
    def salary(self):
        print("40000 is his salary")
    def age(self):
        print("26 is his age")
    def func(obj):

obj.name()
obj.salary()
obj.age()

obj_emp1 = employee1()
obj_emp2 = employee2()

func(obj_emp1)
func(obj_emp2)