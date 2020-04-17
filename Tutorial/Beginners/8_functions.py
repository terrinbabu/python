##############
# fuctions ###
##############
# functions - instructions packeged together to perform a specific task


def hello_func():  # parameter goes inside (), here there is no parameter
    pass  # to leave the function empty


print(hello_func)  # doesnt run but gives the memory of the function
print(hello_func())  # runs the function

# function are helpful to keep your code "dry"
# i.e. not to repeat the same mistake again


def hello_func_1():
    print('Hello Functions')


hello_func_1()

################################
# return a value in function ###
################################


def hello_func_2():
    return'Return\'s Hello Functions'


hello_func_2()  # gives nothing
print(hello_func_2())

# consider functions as with just input and outputs
# example
print(len('Test'))
# fuction "len"
# input - string
# output - int which is lenght of the string
# doesnt care about the code in the functions

# use the retuned value
print(hello_func_2().upper())

#########################################
# create parameter and pass arguments ###
#########################################


def greeting_func(greeting):
    return f'{greeting} Function.'


print(greeting_func('Hi'))


# more arguments and default value

def greeting_func_2(greeting, name='You'):
    return f'{greeting} Function, {name}'


print(greeting_func_2('Hi'))
print(greeting_func_2('Hello', 'Terrin'))


# arbitary numbers of positional and keyword argument
# args - positional arguments (sequences - lists, tuples,..)
# kwargs - keyword arguments (dictionaries)
# *,** - used to tell we dont know how many arguments passed

def student_info(*args, **kwargs):  # args, kwargs - names are conventions
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

# fuction call with arguments starting with * and **

courses = ['Math', 'CS']
info = {'name': 'Mary', 'age': 25}

student_info(courses, info)  # puts courses and info as only args and no kwargs
student_info(*courses, **info)  # puts as args and kwargs
