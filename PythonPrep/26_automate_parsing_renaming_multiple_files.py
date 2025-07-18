# writing python script to automate multiple file remaining

import os

os.chdir('D:\Books')
print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)  # splits extension and filename and returns both in a tuple
    print(file_name)