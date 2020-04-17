########################
# print and variable ###
########################

print("Hello world 1")

# variable #
# by convention - variable are all lower case,
# and underscore(_) is used in middle if writing two letter variable,
# variable should be as describtive than just i,m,k...

message_1 = 'Hello World 2'
print(message_1)

######################################
# single, double and triple quotes ###
######################################

message_2 = "Hello world 3"
message_3 = 'Sunny\'s world'
message_4 = "Bobby's world"
message_5 = 'John"s world'
message_6 = """Bobby's Says
Hello world"""

#################################
# access character of string ####
#################################

print("length of string message_1 : ")
print(len(message_1))
print("Access the 1st character message_1 : ")
print(message_1[0])  # index starts at 0
print("Access-1 (slicing) the 1st word message_1 : ")
print(message_1[0:5])  # starting from 0 till 4 (5 not included)

###################################
# Methods of String data types ####
###################################
# Methods and fuctions are basically same,
# a method is a fuction that belong to an object

print(message_1.lower())  # lower case
print(message_1.upper())  # upper case
print(message_1.count('Hello'))  # counts how many word/letter in the String
print(message_1.count('l'))
print(message_1.find('World'))  # place where the first word/letter starts
print(message_1.find('l'))
print(message_1.find('Terrin'))  # returns a -1
print(message_1.replace('World', 'Universe'))  # replace a word/letter

print(message_1)
message_1.lower()  # doesn't change the string as method return a new string
print(message_1)

message_lower = message_1.lower()
print(message_lower)

#####################
# Adding a string ###
#####################

two_message_1 = message_1 + ' this is ' + message_3 + '. Welcome!'
# the above method gets a bit complicated so using formated string
two_message_2 = '{} this is {}. Welcome!'.format(message_1, message_3)
# {} is called place holder
# for python 3.6 or higher "f-string" functionality exist
two_message_3 = f'{message_1} this is {message_3}. Welcome!'
two_message_4 = f'{message_1} this is {message_3.upper()}. Welcome!'

##################
# Help fuction ###
##################

print(dir(message_1))  # gives all the atributes and methods available
# print(help(str))  # help string data types
print(help(str.lower))
