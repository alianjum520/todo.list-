import re 
str = "We need to inform him with the latest information"
#Generating iterator to find the starting and ending index of string
for i in re.finditer('inform',str):
    tup = i.span()
    print(tup)

print('\n')
#Match anything that ends with at
str2 = "Sat,hat,mat,pat"
allstr = re.findall('[Shmp]at',str2)
for i in allstr:
    print(i)
print('\n')

# All words that are in between h and m
allstr2 = re.findall('[h-m]at',str2)
for i in allstr2:
    print(i)
print('\n')
# All the words except the carrot symbol words like ^h-m no words between these ranges
allstr3 = re.findall('[^h-m]at',str2)
for i in allstr3:
    print(i)
print('\n')
#To replace a certain word through regex 
str3 = "He is a bad boy"
exp = re.compile('[b]ad')
str3  = exp.sub('good',str3)
print(str3)
print('\n')
#Solving backslash problem
str4 = "He is a \\bad boy"
print(re.search(r"\\bad",str4))
print('\n')
#Treating the blank spaces in regex
str5 = '''
keep the blue flag
flying high
Chelsea
'''
print(str5)
exp1 = re.compile('\n')
str5 = exp1.sub(' ',str5)
print(str5)
print('\n')
#  get expression for numbers
number = "0322-7378707"
if re.search('\w{4}-\w{7}',number): #curly brace 4 shows will have 4 digits and 7 shows will have 7 digits   
    print("ok")