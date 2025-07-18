# File objects

f = open('text.txt', 'r')  # name is fine as long as the fie is in the same directory. Otherwise, full path needed
# 2nd arg is the mode in which we need the file
print(f.name)
f_contents = f.readlines()  # returns a list of all lines
print(f_contents)
f.close()  # necessary

# alternatively we could use a context manager to manage opening and closing of file
# with helps us do file tasks within a block
print('')
with open('text.txt', 'r') as j:
    print(j.read(10))  # reads character and takes number of characters as arguments
    # print(f_contents, end='')
    for line in j:  # to get lines from a file one at a time
        print(line, end='')
    print('Done')


# To read a large file

with open('text.txt') as file:
    size_to_read = 10
    f_contents = file.seek(0)  # sets the position at a specific location
    f_contents = file.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        print(file.tell())  # tells the position at which we are in the file

        f_contents = file.read(size_to_read)  # update f_contents with next 10 characters


with open('test.txt', 'w') as wf:  # if the file doesn't already exist it will create it otherwise overwrites
    wf.write('Test')
    wf.write('Test')  # continues writing where it left off
    wf.seek(0)  # get to desired position and then write. If character already exists then it overwrites
    wf.write('Test2')
    print('Done')
    # 'a' is used to append to an existing file