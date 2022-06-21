class employee():
    def __init__(self):

        self.__maxearn =1000000
def earn(self):
    print("earning is:{}".format(self.__maxearn))


def setmaxearn(self,earn):

self.__maxearn=earn

emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setmaxearn(10000)
emp1.earn()