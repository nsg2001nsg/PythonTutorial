li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

s_li = sorted(li, reverse=True)  # function returns new sorted list. Reverse=True, sorts list in descending order
# function sorted works on any iterable
print(s_li)
print(li)
li.sort(reverse=True)  # method sorts the list in place returns none. Works specifically on list
print(li)

tup = (9, 3, 5, 1, 7, 2, 8, 4)
# tup.sort()  # doesn't work for any other iterable except lists
s_tup = sorted(tup)
print(s_tup)

diction = {'name': 'Nandini', 'age': 23, 'gender': 'Female'}
s_dict = sorted(diction)  # sorts key by default
print(s_dict)

i_li = [-3, 2, 1, 9, -4, -1, -7, 0, 5]
s_i_li = sorted(i_li, key=abs)  # key arg runs each element through abs func before sorting
print(s_i_li)

# key arg helps sort elements based on a specific attribute using function


from operator import attrgetter


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, Rs.{self.salary}"


e1 = Employee('Nandini', '23', '100000')
e2 = Employee('Riya', '23', '10000')
e3 = Employee('Priya', '25', '80000')

employees = [e1, e2, e3]

# custom function to for key to return attribute based on which sorting will happen


def get_name(emp):
    return emp.name


s_emp = sorted(employees, key=get_name)
print(s_emp)

a_emp = sorted(employees, key=attrgetter('age'))  # attrgetter returns attribute from an object
print(a_emp)

