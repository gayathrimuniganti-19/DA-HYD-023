#Strings --> Group of characters, we use single or double or triple quotes
#for representation of strings...
#strings are immutable,ordered,indexed collection
#in python space is also a character
'''
name = 'Codegnan'
print(name)
print(type(name))
print(len(name)) #len --> returns the number of items in container

#index() --> fetch the object (position) starts at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25])#indexError ---> as its out of range

#Negative Indexing --> -1 to len(obj)
print(name[-1]) # it returns last char's
print(name[-3])
#print(name[-33])# indexError

#slicing --> we can access group of charaters(objects)
#we use[start:end]#start default ---> 0, start is included, end is excluded
name = 'Gayathri'
print(name[:])# returns entire string
print(name[0:])# returns the entire str
print(name[:4])# starts at 0th index before 4th index
print(name[1:5])
print(name[:6])
print(name[4:])
print(name[5:7])

name = 'python'

print(name[3:7])
print(name[7:3]) #returns as empty strs asre immutable
#Slicing is applicable from lower index to higher index
print(name[:45]) # returns till end of the str
print(name[45:])
#negative slicing
print(name[-1:-5])# returns empty str
print(name[-5:-1])#starts at -5 and ends at -2
print(name[-3:])
#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])

# +ve and -ve
print(name[1:-2])
print(name[2:-6])#returns an empty str
'''
'''
#Task
#observe +ve, +ve, -ve, -ve, & +ve,-ve all possibilities

#striding --> [start:end:step]
course = 'DataAnalysis'
print(len(course))
#Data ---> result
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::1])#returns all char's
print(course[::2])#(0-->n-1) include start to end skipping one char
print(course[1:6:3])#[1:6] --> ataAn ---> [1:6:3] ---> aA
print(course[2::3])#tnys
print(course[::-1])#it returns the reverse of the str
print(course[::-2])
print(course[:-4:])
print(course[:2:4])
print(course[2:4:6])
print(course[-2:-4:-6])
print(course[:-5:])
print(course[1:-3:2])
print(course[:-4:-1])
'''
#Task : workout with all possiblities of slicing and striding on a example

name = 'codegnan'
#name[3] = 'w' # str are immutable
#Operations on Strings ---> Indexing, Concatenation, Reptition,membership
print(name*3)
print('%' * 22)#repitition

#Concatenation --> combining strings

data = 'gayathri' + 'python' + ' ' + 'database'
print(data)
print('1234' * 5)#numeric str
print('gaya' in 'gayathri')
for i in 'gayathri':
    print(i,':')
#in above case we get every char line by line

for i in 'gayathri':
    print(i,end=' ')

name = "dataCodegnan"
#Built-in functions --> len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name))#returns a list sorting all elements

#methods on str --> case-conversion , finding/searching...
name = 'Codegnan data'
#case-conversion --->upper(),lower(),title(),caplitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#Caplitilize() ---> converts first letter to uppercase
c = name.capitalize()
print(c)
d = name.title()#converts every word first letter to uppercase
print(d)

#Task : A B S D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z














