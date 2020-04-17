##################
# dictionaries ###
##################

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CS']}
# dic = {key : value, ...}
# values can be of any data type
# key can be any immutable data type

print(student)
print(student['name'])

# get method
# print(student['phone'])  # give a key error as its not a key
print(student.get('phone'))
print(student.get('phone', 'N/A'))  # default value for absent key

# add/ change entry
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)

# add/change many entries
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CS']}
student.update({'name': 'Jane', 'age': 28, 'phone': '555-5555'})
print(student)

# delete entry
del student['age']
name = student.pop('name')
print(student)
print(name)

#################
# looping dic ###
#################

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CS']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())  # both students and values

for i in student:
    print(i)  # print only keys

for key, value in student.items():
    print(key, value)
