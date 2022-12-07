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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay 

    def __len__(self):
        return len(self.fullname())

# class Developer(Employee):
#     raise_amt = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):

#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_employee(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)


#     def remove_emp(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

    
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())

# dev_1 = Developer('Myers', 'Butera', 50000, 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(issubclass(Manager, Developer))

# print(mgr_1.email)

# mgr_1.add_employee(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps() 

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

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

print(len('emp_1'))


# print(emp_1 + emp_2)
# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())



# import datetime 
# my_date = datetime.date(2022, 12, 6)

# print(Employee.is_workday(my_date))

# emp_1.set_raise_amt(1.05)

# # print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# # print(Employee.num_of_emps)

