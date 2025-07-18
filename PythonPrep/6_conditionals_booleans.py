# Conditionals
# if True:  # default true
#     print('Conditional was true')

language = 'Python'  # python re-uses identical, immutable literals  that appear in the same code file.Thus, both variables point to same object
language2 = 'Python'
str1 = 'Py'
str2 = 'thon'
str3 = str1 + str2  # str3 is assigned at runtime. Thus, doesn't point to the existing object

print(id(language))
print(id(language2))
print(str3)
print(id(str3))

if language == 'Python':   # Checks if the value is same
    print('Python')
elif language == 'C++':
    print('C++')
else:
    print('No match')

if language is language2:  # checks if it's the same exact object in memory
    print('Yay')

# Boolean operations
# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if user == 'Admin' or 'Guest' and not logged_in:
    print('Please Log in')

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)  # true because tuple is immutable

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # false because list is mutable

# a is b means id(a) == id(b)

# False Values

# False
# None
# Zero of any numeric type
# Empty sequences: (), [], ''.
# empty mapping: {}







