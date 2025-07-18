# # First-Class Citizen (Programming)
# A First-class citizen/first class object is an entity which supports all
# the operations generally available to other entities. These operations typically
# include being passed as an argument, returned from a function, and assigned to a variable

# First-class Functions:
# A programming language is said to have first-class functions if it treats functions as first-class citizens
# we should be able to treat functions like any other object or variable


def square(x):
    return x * x


f = square  # function is being assigned to a variable

print(f)
print(f(5))  # variable can now be used as a function


# any function that can take another function as an argument is an example of a high class function


def my_map(func, arg_list):  # takes function as an argument
    result = list()
    for i in arg_list:
        result.append(func(i))  # just for example of function otherwise list comprehension can be used
    return result


def cube(x):
    return x ** 3


l = [2, 3, 4, 5]
answer = my_map(cube, l)
print(answer)


# function that can br returned by another function


def logger(msg):

    def log_message():
        print(f'Log, {msg}')

    return log_message  # returns another function


log_hi = logger('Hey!')
log_hi()  # we execute the returned function as we like
# it remembers the msg first passed because of closure(another tutorial)


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text  # returns a wrapping function with desired tag


header = html_tag('h1')
header("Tittle")
