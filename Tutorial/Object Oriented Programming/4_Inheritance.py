###########################
# Inheritance/Sub-class ###
###########################
# allows to inherit attributes and methods from a parent cls
# we get all the functionalities of the parent cls and also,
# override/add new functionalities without affecting the parent cls


class Employee:  # parent class
    raise_amount = 1.04  # Cls Var-1

    def __init__(self, first, last, pay):  # constructor
        self.first = first  # Obj var-1
        self.last = last  # Obj var-2
        self.pay = pay  # Obj var-3

    def apply_raise(self):  # obj method which uses cls var-1
        self.pay = self.pay * self.raise_amount


class Developer(Employee):  # subclass - Inheritance
    raise_amount = 1.10  # changes the cls var-1, but only changes in subclass


emp_1 = Employee('John', 'Schafer', 50000)  # 1st Obj
emp_2 = Employee('Testa', 'Usera', 60000)  # 2nd Obj

dev_1 = Developer('Corey', 'Tel', 50000)  # 1st Obj of subclass
# this checks for __init__ method in Developer class, if not found,
# It check in the Employee Class
# the order in which it checks is called the method resolution order
# find the order and other details like inherited methods & attributes by,
# print(help(Developer))

print(emp_1.pay)  # 50000
print(dev_1.pay)  # 50000
emp_1.apply_raise()  # uses original cls var-1 value
dev_1.apply_raise()  # uses changed cls var-1 value
print(emp_1.pay)  # 52000
print(dev_1.pay)  # 55000


#########################
# Initialize subclass ###
#########################
class Employee_class:  # parent class
    def __init__(self, first, last, pay):  # constructor
        self.first = first  # Obj var-1
        self.last = last  # Obj var-2
        self.pay = pay  # Obj var-3


class Developer_class(Employee_class):  # subclass - Inheritance
    def __init__(self, first, last, pay, language):  # constructor
        super().__init__(first, last, pay)  # or
        # Employee_class.__init__(self, first, last, pay)
        # this helps use the initialized obj vars in the parent cls
        # super() is better as it works in also with multiple Inheritance
        self.language = language


emp_3 = Employee_class('John', 'Schafer', 50000)  # 1st Obj
emp_4 = Employee_class('Testa', 'Usera', 60000)  # 2nd Obj

dev_2 = Developer_class('Corey', 'Tel', 50000, 'python')  # 1st Obj of subcls

#############################
# some built-in functions ###
#############################

print(isinstance(emp_3, Developer_class))  # false
# checks if arg1 is an obj of the arg2
print(issubclass(Developer_class, Employee_class))  # true
# checks if arg1 is an subcls of the arg2
