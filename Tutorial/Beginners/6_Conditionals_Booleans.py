###########################
# if,elif,else statment ###
###########################

if True:
    print('Conditional was True')

language = 'Python'

if language == 'Python':
    print('Conditional was True')

# else statment
language = 'Java'

if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# elif statement
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# python doesn't have a switch case statement
# as, if,elif and else is pretty clear in python

##################
#  Comparisons ###
##################

# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# Object Identity
# check if two objects have same id (memory)
a = [1, 2, 3]
b = [1, 2, 3]  # stores in different memory if its lists, not if int,string..
# b = a # stores in same memory

print(a == b)  # True
print(a is b)  # False - as they have different id

print(id(a))
print(id(b))

print(id(a) == id(b))  # This is what "is" Conditional does

#########################
#  Boolean operations ###
#########################

# and # or
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
elif user == 'Admin' or logged_in:
    print('Admin Page or logged in')
else:
    print('Bad Creds')

# not - used to switch a Boolean
logged_in = False

if not logged_in:
    print('Please logged in')
else:
    print('Welcome')

##############################
# which gives False Values ###
##############################

condition_1 = False  # False
condition_2 = None  # None
condition_3 = 0  # Zero of any numeric type
condition_4 = []  # Any empty sequence. For example, '', (), [].
condition_5 = {}  # Any empty mapping. For example, {}.

if condition_4:  # check for other conditions
    print('Evaluated to True')
else:
    print('Evaluated to False')

# so,everything else will give True, for example
condition_6 = 'Test'
if condition_6:
    print('Evaluated to True')
else:
    print('Evaluated to False')
