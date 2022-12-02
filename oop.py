class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)