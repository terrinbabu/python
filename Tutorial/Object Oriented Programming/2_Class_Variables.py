####################
# Class Variable ###
####################


class Employee_class:
    raise_amount = 1.04  # Class Variable-1

    def __init__(self, first, last, pay):  # constructor
        self.first = first  # Object variable-1
        self.last = last  # Object varialbe-2
        self.pay = pay  # Object variable-3

    def apply_raise(self):  # object method which uses class variable-1
        self.pay = self.pay * Employee_class.raise_amount


emp_1 = Employee_class('John', 'Bob', 50000)  # 1st Object

print(emp_1.pay)  # object variable-3 of 1st Object
print(Employee_class.raise_amount)  # class variable-1
Employee_class.apply_raise(emp_1)  # object method which uses class variable-1
print(emp_1.pay)  # object variable-3 of 1st Object

#######################################
# Class Variable Vs Object variable ###
#######################################


class Employee_class_1:
    raise_amount = 1.04  # Class Variable-1

    def __init__(self, pay):  # constructor
        self.pay = pay  # object variable-1

    def apply_raise(self):  # object method
        self.pay = self.pay * self.raise_amount  # notice here,
        # we use object variable insead of class variable but,
        # raise_amount is not an object Variable,
        # but still it works, but in a slightly different way


emp_2 = Employee_class_1(50000)  # 1st object
emp_3 = Employee_class_1(60000)  # 2nd object

print(emp_2.__dict__)  # name-spaces of the object, doesn't have raise_amount
print(Employee_class_1.__dict__)  # name-spaces of the Class, has raise_amount

print(Employee_class_1.raise_amount)  # 1.04 - class variable-1
print(emp_2.raise_amount)  # 1.04 - class variable-1
# This works because, when we try to access an atribute on a object,
# it will first check if the object contain the atribute or else,
# it will check if the class or any class that it inherites from has it

Employee_class_1.apply_raise(emp_2)  # object method
print(emp_2.pay)  # object variable-1

#######################################
# changing the Class variable value ###
#######################################

# changing using class
Employee_class_1.raise_amount = 1.05  # changing class variable-1
print(Employee_class_1.raise_amount)  # 1.05 - class variable-1
print(emp_2.raise_amount)  # 1.05 - class variable-1
print(emp_3.raise_amount)  # 1.05 - class variable-1

# changing using object - doesn't work
emp_2.raise_amount = 1.07  # this doesn't change the class variable but,
# create a new object variable-2
print(Employee_class_1.raise_amount)  # 1.05 - class variable-1
print(emp_2.raise_amount)  # 1.07 - object variable-2
print(emp_3.raise_amount)  # 1.05 - class variable-1

print(emp_2.__dict__)  # it has raise_amount now as object variable

Employee_class_1.apply_raise(emp_2)  # object method uses object variable-2
Employee_class_1.apply_raise(emp_3)  # object method uses class variable-1
print(emp_2.pay)
print(emp_3.pay)
# the values are different because in class,
# "self.pay = self.pay * self.raise_amount" was used and not,
# "self.pay = self.pay * Employee_class_1.raise_amount"
# useful if we have to just change the amount of pay raise for each emp


#########################################
# Class Variable - another example    ###
#########################################

class Employee_class_2:
    no_of_emp = 0  # Class Variable-1

    def __init__(self, name):  # constructor
        self.name = name  # object variable-1
        Employee_class_2.no_of_emp += 1  # using Class Variable-1
        # here self.no_of_emp doesnt work


emp_4 = Employee_class_2('peter')  # 1st Object
emp_5 = Employee_class_2('john')  # 2nd Object

print(Employee_class_2.no_of_emp)  # Class variable-1
print(emp_4.no_of_emp)  # Class variable-1
