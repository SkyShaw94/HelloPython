print('Hello World!! This is my first Python script')
print("Woah' example of double and single quotes'")
print("String "+"Combination")
print("Comma","adds space between words")
print("Can print a number as well like,Hi",5)
print("Comments are not printed")
# Single line comment
print("Multiple line comments are done in triple quotes '''")
'''
A multiple line comment
'''
print("================Maths===================")
print("Add 2+5:",2+5)
print("Subtract 6-2:",6-2)
print("Multiply 2*3:",2*3)
print("Divide 4/2:",4/2)
print("Float Divide 5/2:",5/2)
print("Exponent 2**2:",2**2)
print("=================END=====================")

print("=================VARIABLES=====================")
print("VARIABLES ACT AS A PLACE HOLDER HOLDS VALUES COMMON OPERATIONS AND RESULTS OF FUNCTION, etc")
exvar  = 55+22
print("'exvar' holds the value of operatio 55+22=",exvar)
print("====================END=========================")
print("====================UNPACKING=========================")
# Unpacking is an integral part of python where multiple assignment can be done to different VARIABLES
x,y = (5,6)
print("The statement 'x,y=(5,6)' assigns 5 to x & 6 to y")
print("Here the list (5,6) is unpacked into x & y")
print("X=",x)
print("Y=",y)
print("Now if we try to do this 'x,y=(5,6,8)' the python compiler will show an error as we are trying to unpack more values as compared to the number of variable")
print("=======================END==============================")
print("====================WHILE LOOP=========================")
print("'While loop' prints or does some operations untill a certain condition is satisfied")
# var+1 will yield a value but var +=1 will assigns
condition = 1;
while condition <= 10:
    print(condition)
    condition+=1

'''
INFINITE LOOP

while True:
    print(something)

TO BREAK ANY SCRIPT PRESS ctrl+c this is keyboard interruption
'''
print("=======================END==============================")
print("=======================For Loop==============================")
print("'for loop' can be used to iterate through a list")
#Can't assign exlist,var = [1,2,3,4,5,6,7,8,9,10] bcz no has to be equal on both sides
examplelist = [1,2,3,4,65,654,7,842,7539,1098]
# A variable 'eachnum' is created and it is assigned the values of the list in order
'''
Indentation is very important in Python a tab space is automatically added
if not then we have to add unlike other programming languages where {} is sufficient
to define the boundary of the statement within the loop if the statement are Indented
then only those will be executed
'''
for eachnum in examplelist:
    print(eachnum)
'''
range(x,y) is a generator funtion to generate number starting from x increment by 1
till y-1
'''
print("Range Example:")
for x in range(1,11):
    print(x)
print("=======================END==============================")
# 'if' stmt adds some logic to our programming
print("=======================If Stmt==============================")
x=5
y=8
z=3
a=2
print("Single if")
if x<y:
    print("x is less than y")
#Multiple comparisions can be done
print("Multiple comparisions if")
if x<y>z>a:
    print("y is greater than both x, y & a")
'''
== comapares if equal
!= Not equal
<  less than
>  greater than
<= less than equal
>= greater than equal
'''
print("if-else example")
# if-else
if x>y:
    print("x is greater than y")
else:
    print("x is less than y")
'''
Multiple if is applied then
as soon as the stmt is true it breaks
from the Multiple if-else
'''
if x>y:
    print("x is greater than y")
if x<55:
    print("x is less than 55")#terminates here doesnt goto the else stmt this runs as a block which terminates when any condition is True
else:
    print("x is less than y")
print("=======================If-Elif Stmt==============================")
if x>y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
elif x>z:
    print("x is greater than z")
else:
    print("If-Elif stmt didn't work")
print("=======================END==============================")
'''
Define the funtion using keyword 'def' this notifies python of the impending funtion definition
SYNTAX:
def funtion_name(parameters):
    code to be executed
outside funtion

Here Indentation is only used in place of {}
'''
print("=======================FUNCTION==============================")
def mulplication():
    var=5
    var1=2
    print("Product of 5X2=",5*2)
'''
Here the funtion will not display anything
and has to be specifically called like below
'''
mulplication()
'''
Passing parameters in funtion
'''
def addition(num1,num2):
    addres = num1+num2
    print("Sum of ",num1," & ",num2,"=",addres)
addition(12,8)# Also be done as addition(num1=12,num2=8)
'''
Default parameters are used to assign values
which are the base cases but if needed can be modfied
'''
def paramexam(num1,num2=5):
    print("Numbers=",num1,num2)
paramexam(2)#Only needs one value as the second parameter has a deafult set value
#Example 2
def default_param_eg2(height,weight,vac='Sunday',average=75):
    print(height,weight,vac,average)

default_param_eg2(172,85)
#if we want to modify only a specific parameter then we can assign it accordingly
default_param_eg2(172,85,average=85)
'''
x=5
def fun():
    x +=5
can't do the above bcz x is not defined to be global
use the keyword 'global'
def fun():
    global x
    x +=5
Now the above code will work
'''

'''
COMMON ERRORS

-Python is an Indented languages like in case of funtion
Errors:
  -"Name error is not defined": typo error eg;
          variable = 5
          print(varaible)
  - EOL error : String not closed within quotes eg;
                x = ' dkjcnsldvn
                print(x)
'''
print("==========================Writing, Appending & Reading to a file===================")
'''
write just enter the data overriding the previous data "Writing" to a file will clear the file
append adds to the previous data
'''
#firstly create a content to store in the file
txt = "My first file handling\nMoved to the next line"
#specify the savefile
savefile = open("examplefile.txt",'w')
'''
open() : to open files
w - write
r - read
etc
1st parameter is the file_name if it doesn't exist,
it is created
2nd parameter is our intention whether we want to read write or append
 '''
savefile.write(txt)#writes the file
savefile.close()#important to close the file bcz we won't be able to do any further operations
appendtxt = "\nNew info appended to the file"
#change file cursor to next line with file_name.write('\n')
appfile = open("examplefile.txt",'a')
appfile.write(appendtxt)#write() here is in append mode
appfile.close()
#read from file
readfile = open('examplefile.txt','r').read()
print(readfile)
readfilelist = open('examplefile.txt','r').readlines()# stores it in a python list helps in excel sheets
print(readfilelist)
# Classes example

class calculator:

    def add(n1,n2):
        print(n1+n2)
    def subtract(n1,n2):
        print(n1-n2)
    def multiply(n1,n2):
        print(n1*n2)
    def divide(n1,n2):
        print(n1/n2)
print("Class example ")
calculator.add(2,3)
'''
FAQ:
SHEBANG LINE: #!/usr/bin/python in linux tells the path to python but not much use in windows we can specify
'''
import importablefile

importablefile.imp()
print("==================================================================")
#User input
user = input("What is your name? ")
print("Hello ",user)
print("==================================================================")
