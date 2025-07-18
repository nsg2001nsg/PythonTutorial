
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list[start:end:step]
# To extract a certain range of elements from a list or string (sublist/substring) is called slicing

print(my_list[0:5])
print(my_list[0:5:-1])  # doesn't print since  it goes from left to right and using -1 in step reverses it
print(my_list[-1:-8])  # doesn't print since it goes left to right, so we need to use -1 in steps (3rd arg) to reverse it
print(my_list[-1:-8:-1])
print(my_list[0:-2])
print(my_list[0:-2:-1])  # doesn't print because goes in the right direction and reversing it changes the direction

sample_string = 'http://xyz.com'

# reverse
print(sample_string[::-1])
print(my_list[::-1])

# slice to get top level domain from string
print(sample_string[-4:])