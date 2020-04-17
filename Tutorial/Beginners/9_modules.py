# when you import a file, it runs all the code while importing
# so, any print statement will be run as well
# import directly if its in the same folder
import my_module  # I1
import my_module as mm  # I2- to shorten the module name
from my_module import find_index  # I3 - import just the function
from my_module import find_index, test  # I4 - import more
from my_module import find_index as fi, test  # I5 - name the function
from my_module import *  # this imports everything but its better not to use
import sys  # the module used to check where python looks for the modules
import module_index  # I6 - importing from other folder

# standard libraries
import random
import math
import datetime
import calendar
import os
#############################
# importing custom module ###
#############################

courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')  # I1
print(my_module.test)  # I1
index = mm.find_index(courses, 'CompSci')  # I2
index = find_index(courses, 'History')  # I3
print(test)  # I4
index = fi(courses, 'Math')  # I5

# path where python looks for modules
print(sys.path)  # path where python looks for modules while importing

##############################
# add a folder to sys.path ###
##############################

# option 1: hard-coding the path to sys.path

# sys.path.append('D:\Python\Tutorial\Beginners\my_module_folder')
# import module_index
#
# Not best looking approach as we are appending before importing and so,
# if you are using autoprep it rearranges and gives error and also,
# the folder is hard-coded and we have to mannually change if the path changes

# option 2: changing the environmental variable
# right click ThisPC(in windows explore),
# go to properties->Advance system settings->Environment Variables...-> New
# Variable Name : PYTHONPATH
# Variable Value : D:\Python\Tutorial\Beginners\my_module_folder
index = module_index.get_index(courses, 'Math')  # I6
module_path = module_index.__file__  # dunder file attribute- location of a module
# dunder means double underscore


########################
# stardard libraries ###
########################

random_choice = random.choice(courses)
rads = math.radians(90)
sin_rad = math.sin(rads)
today = datetime.date.today()
is_leap = calendar.isleap(2020)
current_directory = os.getcwd()
os_module_path = os.__file__
