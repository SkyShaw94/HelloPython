import csv

dob = []
name = []
age = []
fav_color = []
with open('csv_example.csv') as csvfile:
 readCSV = csv.reader(csvfile,delimiter=',')
 for row in readCSV:
     temp = row[0]
     dob.append(temp)
     temp = row[1]
     name.append(temp)
     temp = row[2]
     age.append(temp)
     temp = row[3]
     fav_color.append(temp)
'''
print(dob)
print(name)
print(age)
print(fav_color)
'''
'''
try-except is a block like if else
if the try succeeds then other is not executed
else the except is executed

Note:try-except are used as a final resort
so there should be conditions to handle irregulrities
'''
try:
    person = input('Name of person: ')
    if person in name:
        ind = name.index(person)
        print(person,"Favourite Color is, ",fav_color[ind])
    else:
        print('Person not in the database')    
except Exception as e:
    print(e)
