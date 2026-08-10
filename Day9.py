'''
Strings --> Caseconversion, searching & Finding, string testing methods, Replace, Space removal
'''
'''
#Searching, Finding, Replacing,Joining...
a = 'Codegnan'
print(len(a))
print(min(a))
print(max(a))

b = a.index('g')# it returns the index position
print(b)

c = a.index('n')# it returns only the first occurance
print(c)
d = a.index('n',6)# it returns the next occurance
print(d)
#e = a.index('n',8)#value error
#print(e)
#f = a.index('t')# value error
#print(f)
#g = a.index('n',1,4)#value error
#print('g')
h = a.index('n',2,6)
print(h)
----------
#rindex() --> returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n')#here 'n' is occuring at 7th index
print(c)
#d =a.rindex('n',8)#value error
#print(d)
----------
#count()--->returns the number of items object is repeating
print('Codegnan'.count('n'))
print('code'.count('w'))#it returns 0 as we dont have 'w' in 'code'
print('cadhiafhakfjehfkuaaju'.count('a'))
----------
#find()--->first occurance but it avoid error returns -1 if substring is not found
print('codegnan'.find('r'))#it returns -1
print('codegnan'.find('n'))
print('gayathri bhavani'.find('h'))
print('gayathri bhavani'.count('h'))
print('codegnan'.rfind('g'))
print('codegnan'.rfind('t'))
-----
a = "DataAnalysis"
for i in a:
    #print(i)
    #print(a.count(i))
    print(a.count(i),a.index(i))
----------
#Replacing,Splitting,Joining
#strings are immutable
a = 'codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('bjhcuh#bbakhyd##bevdt#bhbdfwygv#nnxbhghcn#'.replace('#',''))
print(a.replace('x','gayathri'))
------------
#split
a = 'code gayathri python'
print(len(a))
b = a.split()#by default if we have space it splits(returns list)
print(b)
print(len(b))
c = 'code,gayathri,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
--------------
#join(iterable)--->concatenate any number of strings
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('*'.join('Gayathri'))
print(' '.join('Gayathri'))
---------------
#string testing methods ---> it returns the answer in boolean
#isalpha(),isalnum(),isdigit(),isupper(),islower().....
a = 'Codegnan12345'
print(a.isalnum()) #returns True for alphanumeric strings else False
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha())# returns True only for Alphabets
print(a.isdigit())# returns True only for digit string
print('125489671335'.isdigit())
print('1245155'.isnumeric())#this has upper edge (numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
print('codegnan'.endswith('n'))

print('codegnan'.islower())#returns True for all lowercase
print('CODEgnan.'.isupper())#returns True for all uppercase
print('Code Python'.istitle())
-----------
#space removal----> strip() it removes leading and trailing spaces
a = ' codegnan '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill()--> filling with zeros as per the given numeric string
print('125'.zfill(4))
print('125'.zfill(7))
#center(),ljust(),rjust() ---> Alignment of strings(check length and then modify the width accordinglu)
print('hello'.center(6))
print('hello'.center(8,'*'))

print('hai'.ljust(6,'^'))
print('hai'.rjust(6,'$'))






