class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amt = 1.10

dev_1 = Developer('Myers', 'Butera', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

# print(dev_1.email)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

    # @classmethod
    # def set_raise_amt(cls, amount):
    #     cls.raise_amt = amount 

    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str_1.split('-')
    #     return cls(first, last, pay)

    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True

# print(Employee.num_of_emps)

emp_1 = Employee('Butera', 'Myers', 40000)
emp_2 = Employee('Test', 'User', 30000)

# import datetime 
# my_date = datetime.date(2022, 12, 6)

# print(Employee.is_workday(my_date))

# emp_1.set_raise_amt(1.05)

# # print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# # print(Employee.num_of_emps)

