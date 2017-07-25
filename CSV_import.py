import csv
'''
CSV - Comma Seperated Variables
CSV have commas as delimiter but in
Python we can have anything as a delimiter
'''
'''
simple opening and reading OPERATIONS
with open('csv_example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
'''

'''
Note- Everything will be imported as a string
so we have to convert it before manipulations
'''
DOB = []#empty list
Name = []
with open('csv_example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        date = row[0]
        n = row[1]
        DOB.append(date)
        Name.append(n)
# We have two seperate list
print(DOB)
print(Name)
