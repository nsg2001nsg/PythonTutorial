# try covers a piece of code that might throw an error

try:
    file = open('test.txt')
    # var = bad_var
except FileNotFoundError as e:  # special type of error. More specific errors should be before general ones
    print("Sorry this file does not exist.")
# except Exception as e:   # General Exception catches a variety of errors
#     print(e)
else:  # runs only when no exception is thrown
    print(file.read())
    file.close()
finally:  # Runs regardless to make sure things that need to be done happens at the end.
    print('Executing finally...')


try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception  # raise an error of our own
except Exception as e:
    print("Error!")
