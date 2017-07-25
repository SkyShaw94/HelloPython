'''
OS module is used for any kind of directory
operations like changing path or making directories
or deleting them moving them around
'''
import os

currdir = os.getcwd()#cwd:current working directory
print(currdir)
os.mkdir('name')#make new directory

import time

time.sleep(2)#waits 2 seconds
os.rename('name','NewName')
time.sleep(2)

os.rmdir('NewName')#Removes new directory
# os.rmdir('name')#Removes new directory
# os.rmdir('name1')#Removes new directory
