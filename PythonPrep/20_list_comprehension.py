nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = []

for n in nums:
    my_list.append(n)
print(my_list)

# using list comprehension
# I want "n*n" for each n in nums
my_list = [n*n for n in nums]
print(my_list)

# I want n if n is even
my_list = [n for n in nums if not n % 2]
print(my_list)

# I want a letter number pair from 0123 and abcd
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]  # nested loop
print(my_list)


# Dict comprehension
names = ['Brad', 'Henry', 'Matthew', 'Jake', 'Channing', 'Ryan']
surnames = ['Pitt', 'Cavil', 'McConaughey', 'Gyllenhaal', 'Gosling']

# zip is used to combine iterables (list, tuples etc) element-wise, Widely used for parallel iteration, creating dictionaries and unzipping
# my_dict = {}
# for name, surname in zip(names, surnames):
#     my_dict[name] = surname

my_dict = {name: surname for (name, surname) in zip(names, surnames)}
# my_dict = dict(zip(names, surnames)) # another way

print(my_dict)


# set comprehensions

num = [1,1, 2,2, 2, 2, 4, 3, 3, 3]
# my_set = set(n for n in num)
my_set = {n for n in num}
print(my_set)


# generator expressions
# I want to yield



