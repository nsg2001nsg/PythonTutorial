# A CSV (Comma Separated Values) file is a plain text file format used to store tabular data,
# such as spreadsheets or databases.

import csv
with open('sample_contacts.csv', 'r') as cfile:
    csv_reader = csv.reader(cfile)  # by default reader expects comma separated value
    next(csv_reader) # jumps to next record
    for line in csv_reader:
        # print(line)  # returns each record as a list
        if line:
            print(line[1])  # specific index value