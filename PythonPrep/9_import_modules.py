# import custom module (.py file created in the sam dir)
# sys.path.append('path/to/directory') # not the best approach. Rather add path to environment variables
import random
import datetime
import calendar
import os  # gives access to underlying os
import  webbrowser

import custom_module as cm  # creating an alias
from custom_module import hello  # another way to import a specific function
# or from custom_module import * (import everything )

print(cm.greeting('Hey Beautiful!'))
hello()

# sys.path has a list of all directories where import looks for modules
# we can manually add path to a directory to sys.path  using append method (Not the best approach)


# Some general modules from standard library
courses = ['Math', 'Computer Science', 'Literature']
random_course = random.choice(courses)  # To get a random element
print(random_course)

print(datetime.date.today())  # To get today's date
print(calendar.isleap(2025))  # To check for leap year
print(os.getcwd())  # To get the current working directory
print(os.__file__)  # To locate the module itself. The entire standard library is located here
webbrowser.open("https://xkcd.com/353/")  # opens a web page


# + os.getcwd()                                            => get current working directory
# + os.chdir(<path>)                                    => change directory
# + os.listdir()	                                            => list directory
# + os.mkdir(<dirname>)                           => create a directory
# + os.makedirs(<dirname>)                    => make directories recursively
# + os.rmdir(<dirname>)	                   => remove directory
# + os.removedirs(<dirname>)                => remove directory recursively
# + os.rename(<from>, <to>)                   => rename file
# + os.stat(<filename>)                            => print all info of a file
# + os.walk(<path>)	                          => traverse directory recursively
# + os.environ		                                 => get environment variables
# + os.path.join(<path>, <file>)              => join path without worrying about /
# + os.path.basename(<filename>)     => get basename
# + os.path.dirname(<filename>)         => get dirname
# + os.path.exists(<path-to-file>)         => check if the path exists or not
# + os.path.splitext(<path-to-file>)      => split path and file extension
# + dir(os)			                               => check what methods exists