class employee:
    def __init__(self, first, last, sal):
        self.fname = first
        self.lname = last
        self.sal = sal
        self.email = first + '.' + last + '.'


emp_1 = employee('mounika', 'patel', 380000)
emp_2 = employee('srikanth', 'patel', 500000)
print(emp_1.email)
print(emp_2.email)