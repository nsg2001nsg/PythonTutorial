
# Generators do not hold all the values in memory (Efficient)
# If you used a normal function with return, it's like this:

def give_chocolates():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Now, if you use a generator with yield, it's like this:

def give_chocolates_one_by_one():
    for i in range(1, 11):
        yield i
        #  yield pauses the function and remembers where it left off.
        # Next time you ask (calling next()), it resumes from where it paused.
        # They’re memory efficient (especially for big data).
        # You don’t compute everything at once just when needed.
        # Great for loops, streaming, and lazy loading.
        # return says “Here’s everything!”
        # yield says “Here’s one. Ask me again if you want more.”


print(give_chocolates())  # gives the whole list
chocolate = give_chocolates_one_by_one()
print(next(chocolate))  # gives one when asked

my_nums = [x*x for x in range(1, 11)]

nums = (x for x in range(1, 11))  # This is a generator not a tuple comprehension
print(my_nums)
print(next(nums))
print('FOR LOOP')
for n in nums:  # starts generating where it left off
    print(n)

# we can get all the generated values at once by typecasting nums to list but we lose the performance gained by generator