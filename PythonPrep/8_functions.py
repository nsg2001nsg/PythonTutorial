# Function allows to reuse a piece of code without rewriting

# To create a function
def empty_func():
    pass  # leave for later


empty_func()  # does nothing


def hello():  # Takes no arguments
    print("Hello!")  # returns nothing


def message():
    return "Hello!"


print(message().upper())  # using result of one function to call a method


def greet(name):  # Takes an argument (required unless default value is set)
    return f"Hello, {name}! How are you?"


print(greet('Nandini'))


def compliment(text='You look nice!'):  # default arg set
    return f"{greet('Nandini')}. {text}"


# Required args should always appear before default


print(compliment())


def student_info(*args, **kwargs):
    # *args: accepts (extra) multiple positional args and puts them in a tuple
    # **kwargs: accepts (extra) multiple key-worded args and puts them in a dict
    print(*args)  # * unpacks positional args inside the tuple, **
    print(args)
    print(*kwargs)  # * gives out only the keys for kwargs, ** unpacks dict
    print(kwargs)


student_info('Google', 'Amazon', 'Microsoft', 'Myntra', 'Nykaa', name='Nandini Gupta', age=23)

months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]


def is_leap(year):
    """Returns True for leap year and False for non-leap years"""  # doc string - defines what a function does
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month!'

    if month == 2 and is_leap(year):
        return 29

    return months_days[month]


