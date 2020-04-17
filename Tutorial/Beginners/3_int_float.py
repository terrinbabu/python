############################
# integer and float type ###
############################

num = 3
pi = 3.1416

print(type(num))
print(type(pi))

# Arithmetic Operators
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2 - No decimals
# Exponent:       3 ** 2
# Modulus:        3 % 2 - Reminder after division
# Order of operation - PDMAS

# Incremental Operation
num += 1
num *= 10

# Absolute and rounding off
print(abs(-3))  # gives only positive
print(round(pi, 2))  # round to two digit

# Comparisons
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
print(num == pi)

#############
# Casting ###
#############

# strings to numbers
str_num_1 = '100'
num_1 = int(str_num_1)
print(type(num_1))

str_num_2 = '10.34'
num_2 = float(str_num_2)
print(type(num_2))

# number to string
num_3 = 3.5
str_num_3 = str(num_3)
print(type(str_num_3))
