####################################
# Creating Classes and Objects   ###
####################################
# classes are used to logically group datas and functions
# in a class, datas are called attributes and functions are called methods


class Employee_class:
    pass


# objects
# class is a blue-print for creating objects
emp_1 = Employee_class()  # 1st object of employee class
emp_2 = Employee_class()  # 2nd object of employee class
print(emp_1)  # each object has unique memory location
print(emp_2)

###############################
# Creating Object variables ###
###############################

# creating object variables manually
emp_1.first = 'Corey'  # "first" - object variable-1 of 1st object
emp_1.last = 'Schafer'  # "last" - object variable-2
emp_1.email = 'Corey.Schafer@company.com'  # "email" - object variable-3
emp_1.pay = 50000  # "pay" - object variable-4

emp_2.first = 'Test'  # "first" - object variable-1 of 2nd object
emp_2.last = 'User'  # "last" - object variable-2
emp_2.email = 'Test.User@company.com'  # "email" - object variable-3
emp_2.pay = 60000  # "pay" - object variable-4


# creating object variables by intiallize the class attributes
class Better_employee_class:
    def __init__(self, first, last, pay):  # init method - constructor
        # this is an object method, when creating it,
        # they receive the object as the first argument automatically
        # its called "self" by convention
        self.fname = first  # "fname" - object variable-1
        self.last = last  # "last" - object variable-2
        self.pay = pay  # "pay" - object variable-3
        self.email = f'{first}.{last}@company.com'  # "email"-object varialbe-4


emp_3 = Better_employee_class('John', 'Schafer', 45000)  # 1st Object
emp_4 = Better_employee_class('Testa', 'Usera', 60000)  # 2nd Object

print(emp_3.fname)  # object variable-1 of 1st Objects
print(emp_4.email)  # object variable-4 of 2nd objects


###################
# object method ###
###################
class Employee_class_with_method:
    def __init__(self, first, last):  # constructor
        self.first = first  # object variable-1
        self.last = last  # object variable-2

    def fullname(self):  # object method
        return f'{self.first} {self.last}'


emp_5 = Employee_class_with_method('John', 'Bob')  # 1st object

# using the object method
print(emp_5.fullname())  # Or
print(Employee_class_with_method.fullname(emp_5))
