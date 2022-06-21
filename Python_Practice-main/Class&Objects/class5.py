class employee:
    perc_raise = 2.05

    def __init__(self, first, last, sal):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.email = first + '.' + last + '@capgemini.com'

    def fullname(self):
        return '{}{}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.sal = int(self.sal * 2.05)


emp_1 = employee('data', 'base', 390000)
emp_2 = employee('test', 'test', 500000)

print(emp_1.sal)
emp_1.apply_raise()
print(emp_1.sal)

print(emp_2.sal)
emp_2.apply_raise()
print(emp_2.sal)