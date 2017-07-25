'''
Regex:
Used to parse paragraph data away from HTML
data
'''
'''
Identifiers:(looks for number)
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers:(looks for this amt or type)
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

. + * ? [ ] $ ^ ( ) { } | \
Brackets:

[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z

'''

import re

teststring = '''
hello there everyone,
right now i'm learning regex;
it is a very useful tool for matching...!!.
Akki is 22 years old and studying computer science
Sky is 23 years old. Jessy is 105 years old
'''
ages = re.findall(r'\d{1,3}',teststring)# To notify Python that its a regular expression use r in Brackets
names = re.findall(r'[A-Z][a-z]*',teststring)

print(ages)
print(names)

#Save in Dictionaries
agedict = {}
c=0
for eachname in names:
    agedict[eachname] = ages[c]
    c+=1

print(agedict)
