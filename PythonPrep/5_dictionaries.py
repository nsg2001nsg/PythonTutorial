# Dictionaries are a key-value pair
student = {'name': 'Nandini Gupta', 'age': 23, 'courses': ['DS', 'Python', 'Database', 'System Design', 'OS', 'AI']}

# student['age'] = 24  (updates age)
# student['gender'] = 'Female'  (appends)

student.update({'age': 23, 'gender': 'Female'})  # takes a dictionary. Can update/append multiple items at once
print(student)

# To delete a key
del student['gender']

# Or use pop to return deleted item
gender = student.pop('age')
print(student)
print(gender)

# To get length of dict
print(len(student))

# To get all items of dict
print(student.items())

# To get all keys
print(student.keys())

# To get all values
print(student.values())

# To traverse through keys
for key in student:
    print(key)

# To get keys and values
for key, value in student.items():
    print(key, value)