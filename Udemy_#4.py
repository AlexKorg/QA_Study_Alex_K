from bdb import GENERATOR_AND_COROUTINE_FLAGS


print('todai'.replace('i', 'y'))
x = [1, 2, 3]

# list datatypes

monday_temperatures = [9.1, 8.8, 7.5, 5.6, 7.9, 3.1, 9.8]

print(monday_temperatures[3:])

print(monday_temperatures[-1])

print(monday_temperatures[-2:])

mystring = 'Hello'
print(mystring[1])
print(mystring[:3])

# dictionaries

student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
print(student_grades['Sim'])

cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)

cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)

cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)
