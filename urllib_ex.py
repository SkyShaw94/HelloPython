'''
urllib allows us to acces the internet using Python

'''
import urllib.request

x = urllib.request.urlopen('https://google.com')
#prints the source code of the webpage
print(x.read())
