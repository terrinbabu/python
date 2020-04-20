#############
# problem ###
#############


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Schafer')

emp_1.first = 'Jim'
print(emp_1.first)  # Jim
print(emp_1.fullname())  # Jim Schafer
print(emp_1.email)  # John.Schafer@company.com - doesn't change,to solve this,
# we can define a method with email but then we have to call it as,
# emp_1.email() but then others who already used this cls will have to change,
# to solve this we use property decorator

########################
# property decorator ###
########################
# allows to define a method but access it like an attribute


class Employee_1:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_2 = Employee_1('John', 'Schafer')

emp_2.first = 'Jim'
print(emp_2.first)  # Jim
print(emp_2.fullname)  # Jim Schafer - accessed a method like an attribute
print(emp_2.email)  # Jim.Schafer@company.com - method like an attribute

# but here, you cant set these "method" like you set other attributes ie,
emp_2.first = 'Jake'  # works
# emp_2.fullname = 'Jim Jake'  # error
# also even if its works, it still doesn't change the first and last obj var
# you need to use a setter

########################
# setter and deleter ###
########################


class Employee_2:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name')
        self.first = None
        self.last = None


emp_3 = Employee_2('John', 'Schafer')

emp_3.fullname = 'Corey Schafer'  # goes to the setter,
# use the fullname method to set the first and last obj vars
print(emp_3.fullname)  # Corey Schafer
print(emp_3.first)  # Corey

del emp_3.fullname  # goes to the deleter

print(emp_3.fullname)  # Corey Schafer
print(emp_3.first)  # Corey
