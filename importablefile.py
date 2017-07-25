def imp():
    print("This is an importable file which can be used with other programs")
'''
'if __name__ == '__main__':'
This line is used to know whether the current
script is running or it is an importable
if the above line is not in used
and we import this python file on another then it will be executed
line by line as the python runs it
But if we run this python file directly
then it will only print those line within
'if __name__ == '__main__':'

'''
if __name__ == '__main__':
    print("Line will not run in the imported file")
