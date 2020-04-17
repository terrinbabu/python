###########
# LIST ####
###########
# format [...]

courses = ['History', 'Math', 'Phy', 'CS']
print(courses)
print(len(courses))
print(courses[0])  # first
print(courses[-1])  # last

# Slicing the list
print(courses[0:2])  # from 0 to 1, 2 - excluded
print(courses[:2])  # from first to 1
print(courses[1:])  # from 1 till end

# Adding to list
courses.append('Art')  # at the end
courses.insert(3, 'Art')  # insert at 3rd position and shift the rest

courses_1 = ['Art', 'Education']
courses.append(courses_1)  # add a "list" at the end - list in list
courses.insert(0, 'courses_1')  # insert a "list" at 0th -list in list
courses.extend(courses_1)  # add the elements of list at end - one list

# Remove from list
courses.remove('Math')
courses.pop()  # remove the last value
popped = courses.pop()  # stores the popped value

# Sorting the list
courses = ['History', 'Math', 'Phy', 'CS']
courses.reverse()
courses.sort()  # in alphabetical/accending order
courses.sort(reverse=True)  # in reverse alpha/decending

sorted_course = sorted(courses)  # without altering the org
sorted_course = sorted(courses, reverse=True)

# Min,max and sum
nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))


# find index
print(courses.index('Math'))

# list to string and vise versa
course_str_hyphen = ' - '.join(courses)
print(course_str_hyphen)

new_courses = course_str_hyphen.split(' - ')
print(new_courses)

###################################
# in operator and looping list ####
###################################

print('Art' in courses)
print('Math' in courses)

for course in courses:  # each time it loops, course = next item in courses
    print(course)  # print by default goes to a new line

for index, course in enumerate(courses):  # gives also the index
    print(index, course)

for index, course in enumerate(courses, start=1):  # start index at 1
    print(index, course)


###########
# TUPLE ###
###########
# can't edit it(immutable)
# format (...)

list_courses = ['History', 'Math', 'Phy', 'CS']
tuple_courses = ('History', 'Math', 'Phy', 'CS')
list_courses[1] = 'Art'
# tuple_courses[1] = 'Art' # gives error as it can't be edited

##########
# SETS ###
##########
# unordered and without duplicates
# format {...}

sets_courses = {'History', 'Math', 'Phy', 'CS'}
print(sets_courses)  # prints in random unorder
sets_courses = {'History', 'Math', 'Phy', 'CS', 'Math'}
print(sets_courses)  # removes the duplicate Math (so only one)

# membership test - used to check if a value part of a set
# list and tuple also can be used but sets are optimized
print('Math' in sets_courses)

# values that shares/not share with other sets
cs_courses = {'History', 'Math', 'Phy', 'CS'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))  # courses in common
print(cs_courses.difference(art_courses))  # courses not in common
print(cs_courses.union(art_courses))  # all the courses

############################
# Empty List,Tuples,Sets ###
############################

# Empty Lists
empty_list = []  # Or
empty_list = list()
# Empty Tuples
empty_tuple = ()  # or
empty_tuple = tuple()
# Empty Sets
empty_set = {}  # This isn't right! It's a empty dictionary
empty_set = set()
