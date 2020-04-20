import datetime
##################
# Class method ###
##################


class Employee_class:
    raise_amount = 1.04  # cls var-1

    def __init__(self, first, last, pay):  # constructor
        self.first = first  # obj var-1
        self.last = last  # obj var-2
        self.pay = pay  # obj var-3

    def apply_raise(self):  # object method (takes obj as first argument)
        self.pay = self.pay * Employee_class.raise_amount  # changes obj var-3

    @classmethod  # decorator, it alters the fuctionality of a method,
    # so now, the method receives class as the first argument
    def set_raise_amt(cls, amount):  # class method, cls - convention
        cls.raise_amount = amount  # changes the cls var-1


emp_1 = Employee_class('John', 'Bob', 50000)  # 1st obj

Employee_class.set_raise_amt(1.05)  # using the class method

print(Employee_class.raise_amount)  # cls var-1
print(emp_1.raise_amount)  # cls var-1

######################################
# using class method to create obj ###
######################################
# a common use case of class method
# used as alternative constructor ie,
# used to provide alternative way to create obj


class New_employee_class:
    def __init__(self, first, last, pay):  # constructor
        self.first = first  # obj var-1
        self.last = last  # obj var-2
        self.pay = pay  # obj var-3

    @classmethod  # alternative constructor (name starts with from-convention)
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')  # gives value to obj var-1,2,3
        return cls(first, last, pay)  # send the obj vars values to constructor


emp_str_1 = 'John-Doe-70000'  # we have to create object from this string
new_emp_1 = New_employee_class.from_string(emp_str_1)  # 1st obj
# here we use class method to find the values of obj vars and then,
# pass those values to cls constructor to create obj
print(new_emp_1.first)


###################
# static method ###
###################
# object method passes object as first argument
# class method passes class as first argument
# static method doesnt pass anything and ,
# it doesnt access an object or class
# it's a regular function but used inside a class because,
# it has some logical connection with the class

class Another_employee_class:
    def __init__(self, first, last, pay):  # constructor
        self.first = first  # obj var-1
        self.last = last  # obj var-2
        self.pay = pay  # obj var-3

    @staticmethod
    def is_workday(day):
        print(day.weekday())  # 0-monday,1-tuesday ...
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_2 = Another_employee_class('John', 'Bob', 50000)  # 1st obj

my_date = datetime.date(2020, 2, 13)
print(Another_employee_class.is_workday(my_date))  # using static method,
# doesnt pass an object or class
