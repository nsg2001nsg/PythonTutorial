# variable names are conventionally all lower case with underscore separating words

# If single quote (') is being used in a string then it can be escaped using a backslash (\)
print('Nandini\'s World')

# or simple use double quotes (") or three ticks (`)
print("Nandini's World")


message = "Nandini's World"
message2 = "Universe"
text = "Hello"
name = "Nandini"

# To get length of string
print(len(message))

# To get a specific character of string use valid index
print(message[1])

# To get a substring use slicing [x:y] (Including x upto but not including y)
print(message[0:7])
# leaving out first or last index in slicing means including the beginning or ending index respectively

# To convert string to lower or upper case
print(message.lower())
print(message.upper())

# To get count of specific word or character (exact match)
print(message.count('World'))

# To get index of word or character
print(message.find('Nan')) # returns -1 if can't find

# To replace substring with new characters
print(message.replace('World', 'Universe')) # doesn't change actual string

# To concatenate strings
print(message[0:9] + " " + message2)

# or
print("{}, {}. Welcome! Using format method".format(text, name))

# or Fstrings
print(f"{text}, {name}. Welcome! Using Fstrings (Formatted Strings)")
# fstrings allow method calls with variables in the placeholder

# To get overview of all the generic attributes/methods available in the program
print(dir(name))

# `To see how to use a specific method
print(help(str.lower))


