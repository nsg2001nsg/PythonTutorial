# LEGB
# Local, Enclosing, global, Built-in
#
x = 'global x'
print(x)


def test():
    y = 'local x'
    global z  # work with global variable inside local scope. Doesn't have to be defined previously
    z = 'global z'
    print(y)
    print(x)  # first checks local scope and then checks global


test()
print(z)
# print(y)  # throws error


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'  # enclosing var (func within func)
        print(x)

    inner()
    print(x)


outer()