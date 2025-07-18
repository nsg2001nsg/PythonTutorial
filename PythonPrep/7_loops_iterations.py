nums = [1, 2, 3, 4, 5]

for num in nums :
    if num == 3:
        print('Found')
        break  # breaks out of the loop
    print(num)

for num in nums:
    if num == 1:
        continue  # skips the iteration
    print(num)

# Nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range
for i in range(10):  # Starting from 0, upto but not including 10
    print(i)

for i in range(1, 10):  # Starting from 1, upto but not including 10
    print(i)

for i in range(1, 10, 2):  # Starting from 1, upto but not including 10, taking 2 steps
    print(i)

# while - loop goes on until a certain condition meets

x = 0
while x < 10:
    print(x)
    x += 1

# Infinite loop   (ctrl c to stopN)
while True:
    print('Hey')


    