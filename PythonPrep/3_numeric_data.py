num = 3

# to get type of variable
print(type(num))

# Arithmetic Operations
add = 3 + 2
print(add)

sub = 2 - 3
print(sub)

mul = 3 * 2
print(mul)

div = 2 / 3
print(div)

floor_div = 2 // 3   # Doesn't give the decimal part
print(floor_div)

exponent = 3 ** 2  # 3 raised to 2
print(exponent)

mod = 3 % 2  # returns remainder
print(mod)
# mod 2 with any number resulting in 0 says the number is even

# Increment decrement value
num += 1
num -= 1
print(num)

# to get absolute value
sub = abs(sub)
print(sub)

# Round values to the nearest integer
div = round(div)
print(div)

# To round to the x digit after the decimal
num2 = 0.6666
print(round(num2, 2)) # Rounds upto the 2nd digit after the decimal


# Comparison operators
# Equal: ==
# Not equal: !=
# Greater than: >
# less than: <
# Greater than or equal to: >=
# less than or equal to: <=

# Type Casting
num3 = '100'
num4 = '101'
print(num3 + num4)  # Concatenates strings
print(int(num3) + int(num4))  # converts to int type and adds
