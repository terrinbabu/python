##############
# for loop ###
##############
# iteration through a certain number of values

courses = ['History', 'Math', 'Phy', 'CS']

for course in courses:  # each time it loops, course = next item in courses
    print(course)  # print by default goes to a new line

for index, course in enumerate(courses):  # gives also the index
    print(index, course)

for index, course in enumerate(courses, start=1):  # start index at 1
    print(index, course)

# loop in loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range
for i in range(10):  # from 0 to 9 (10 items)
    print(i)

for i in range(1, 11):  # from 1 to 10
    print(i)

########################
# break and continue ###
########################

# break - break out of the loop

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

# continue - skip to next iteration
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)


################
# while loop ###
################
# loop keeps going till a certain condition is met,
# or reach a break statement

x = 0
while x < 10:
    print(x)
    x += 1

x = 0
while True:  # infinte loop
    if x == 5:
        break
    print(x)
    x += 1
