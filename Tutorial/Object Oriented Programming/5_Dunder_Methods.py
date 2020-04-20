##################
# repr and str ###
##################
# used to give info of the obj


class Employee:

    def __init__(self, first, last, pay):  # Dunder Method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):  # used to recreate the obj
        # it should be an unambigious representation of the obj
        # its used by developers for debugging and logging
        # good rule is to display that can be copied to recreate the obj
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):  # read-able representation of the obj for end-users
        return f'{self.fullname()} - {self.email}'


emp_1 = Employee('John', 'Schafer', 45000)
emp_2 = Employee('Testa', 'Usera', 30000)

print(emp_1)  # runs __str__ Method, if __str__ Method is not available then,
# it runs __repr__ Method, if its also not available then,
# it prints the class name and memory location of the obj (not what many needs)

# to call them seperately,
print(repr(emp_1))  # or
# print(emp_1.__repr__())
print(str(emp_1))  # or
# print(emp_1.__str__())
# its good to atleast have an repr when making a class as,
# if you call __str__ and its not available it runs the repr method (fall-back)


#########################
# other Dunder method ###
#########################
# actually, the repr and str are normally the only dunder method used
# unless, doing some complicated codings

class Employee_1:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def __add__(self, other):  # adds the pay of two emp
        return self.pay + other.pay

    def __len__(self):  # gives the length of the emp fullname
        return len(emp_1.fullname())


emp_1 = Employee_1('John', 'Schafer', 45000)
emp_2 = Employee_1('Testa', 'Usera', 30000)

# __add__ dunder method,
print(emp_1+emp_2)  # adds the pay of two emp
# "+" calls the __add__ method

# __len__ dunder method,
print(len(emp_2))  # gives the length of the emp fullname
# "len" calls the __len__ calls


# actually when we print two numbers addtion like,
# we are calling the __add__ method on the int obj ie,
print(1+2)  # or
print(int.__add__(1, 2))
# for strings,
print('a'+'b')  # or
print(str.__add__('a', 'b'))
# len of string,
print(len('Test'))
print('Test'.__len__())  # __len__ method on 'Test' str obj
