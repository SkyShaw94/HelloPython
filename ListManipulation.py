'''
As we know List are mutable and we can do
a lot of manipulations as compared to
Tuples
'''
x= [2,35,351,53,35,135,31,35,135,1351,3,51,1312,54,21,4,121,4,1,5,2,1,351]
# .append(data) adds data to the end of the list
x.append(45)
print(x)
#Not necessary datatypes have to be same
x.append('Hello')
print(x)
# .insert(index_no,data)
x.insert(1,99)
print(x)
# .remove(x[index_no])
x.remove(x[1])
print(x)
# Reference data using index_no like x[i]

#SLICING - only a part of the data is selected x[start_index:end_index] print all data excluding the element at the last index_no
print(x[2:10])
#We can access the List from the back using negative indexing
print("The Last element of the List: ",x[-1])
print("The Second Last element of the List: ",x[-2])

# We can know the index of a data present in out list by x.index(data)
print("The index of 351 : ",x.index(351))
# Can have count of a particular data ie no of times it occured
print("Number of occurance of the number 4: ",x.count(4))
x.remove(x[-1])
x.sort()# Sorts in ascending / Also sorts alphabetically if the list is String
print("Sorted List:")
print(x)
y= ["Gaurav","Saurav","Prem","Shaz","Parvinder","Mayank","Aakash"]
y.sort()
print(y)

'''
Multi-Dimentional List
'''
mul_list = [[[5,5],[6,6]],
            [7,8],
            [11,11]
           ]
print(mul_list[0][1])
print(mul_list[0][1][0])
# We can go as further as we like but it gets messy
