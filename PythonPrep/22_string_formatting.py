person = {'name': 'Nandini', 'age': 23}
li = ['Jennifer', 35]
person1 = "My name is {0[name]}. I am {0[age]}yrs old.".format(person)  # string format using dict
print(person1)
person2 = "My name is {0[0]}. I am {0[1]}yrs old.".format(li)  # string format using list
print(person2)


class woman:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p3 = woman('Monica', '36')
person3 = "My name is {0.name}. I am {0.age}yrs old.".format(p3)  # string format using class object
print(person3)

person4 = "My name is {name}. I am {age}yrs old.".format(name='Phoebe', age=39)  # string format using keywords
print(person4)

p5 = {'name': 'Chandler', 'age': 40}
person5 = "My name is {name}. I am {age}yrs old.".format(**p5)  # string format using dict unpacking
print(person5)

for i in range(1, 11):
    print("The value is {0:02}".format(i))  # padding in formatting upto 2 digits using ':'

pi = 3.1415
print("The value of pi is {0:.2f}".format(pi))  # format string to get 2 digits after decimal

print("My salary is Rs.{0:,.2f}".format(10000000))  # To make numbers more readable along with decimal

import datetime

my_date = datetime.datetime(2025, 7, 9, 13, 12, 40)  # year, month, day, hour, minutes, seconds
print(my_date)

print("Today: {0:%a, %b}/{0:%Y}".format(my_date))  # refer python website for datetime formatting

