# Lists
# allows us to work with a list of elements
courses = ['History', 'CompSci', 'Math', 'Science', 'Geography']

# To get number of values in the list
print(len(courses))

# To get value at a specific location using index
print(courses[3])
# Negative indexes starting from -1 (Starts from the last item of list)
# Trying to access index that isn't available throws error

# Slicing
print(courses[2:6])  # Including 2 but upto not including 6

# To add an item to the end of the list
courses.append('Art') # Can append a list itself too as an element

# To  insert value at a specific location
courses.insert(0, 'Gym')
# Shifts all other elements to the right
print(courses)

# We can insert another list too using insert method
courses2 = ['Psychology', 'Literature']
courses3 = []
courses3.insert(0, courses2) # This adds a list itself as an element, not individual elements
print(courses3)

# To add individual elements from one list to another
courses.extend(courses2)
print(courses)

# To delete element
courses.remove('Geography')

# To delete last element of a list
print(courses2.pop(), "Popped")  # pop method returns the element it popped
# Could be used in stack
print(courses2)

# To reverse a list
courses.reverse()
print(courses)

# To sort elements
num = [1, 2, 3, 4, 5]
num.sort(reverse=True) # To sort in ascending order
print(num)

# To get sorted version of a list without altering original list
print(sorted(courses)) # Returns a sorted version of list

# To get min, max and sum of list
print(min(num))
print(max(num))
print(sum(num))

# To get index of a specific value that exists in the list
print(courses.index('Math'))

# To check if an element exists in a list
print('English' in courses)

# To traverse all elements in the list
for item in courses:
    print(item)

# To also access index along with element value
for index, item in enumerate(courses, start=1):  # We can also start index from 1 using start = 1
    print(f"{index} {item}")

# To make a string out of list elements separated by a certain value
courses_str = ', '.join(courses)  # Returns string
print(courses_str)

# To split a string into list of items based on a specific value
new_list = courses_str.split(', ')
print(new_list)

# Tuples (Immutable otherwise similar to lists)
veggies = ('zucchini', 'Avocado', 'Tomato')

# veggies[0] = 'Brocolli' (throws error)

# Sets
# Unique Elements (No duplicate values allowed)
# Order Doesn't matter
# Widely used to remove duplicate values
# To see if an element is part of the set (Can do so much more efficiently than list and tuples) aka Membership test
# To determine what values a set shares or doesn't share with another set

fruits = {'Apple', 'Banana', 'Orange', 'Mango'}
fruits2 = {'Cherry', 'Strawberry', 'Apple', 'Mango'}

print(fruits.intersection(fruits2))
print(fruits.difference(fruits2))
print(fruits.union(fruits2))


# How to create empty list, tuple or set
# list
empty_list = []
empty_list = list()

# tuple
empty_tuple = ()
empty_tuple = tuple()

# set
empty_set = {}  # Incorrect. Creates Dict
empty_set = set()  # Correct







