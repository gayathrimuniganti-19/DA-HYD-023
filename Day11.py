'''
Lists,Tuples...
#List --> mutable,ordered,heterogenous
#index(),count(),copy(),sort(),reverse()
details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21,6))
#print(details.index('python'))-->ValueError
print(details.count(21))
print(details.count('python'))#it returns the 0 where we dont have python in list
-----
#we can also write yesterday task as below
data = ['Codegnan','Gayathri','python','java']
for obj in data:
    print(data.index(obj),':',obj)
#in range()
for obj in range(len(data)):
    print(obj,':',data[obj])
--------
#copy()--->shallow copy of the given collection
data = ['Codegnan','Gayathri','python','java']
new = data.copy()
print(new)
print(type(new))
print(data)
new[2] = 'Agentic AI'
print(new)
print(data)
data.append('Gayathri')
print(data)
print(new)
--------
data = [1,5,7,[8,6,78,57],25]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents'#whenever we make changes in nested list odiginal will be also affected
print(new)
print(data)

new[1] = 'Python'
print(new)
print(data)
-------
marks = [14,24,-45,27,35]
print(marks)
print(marks.sort())#returns None
print(marks)#returns in ascending order
marks.sort(reverse = True)#returns in Descending order...
print(marks)
marks.insert(65,'Gayathri')
#marks.sort()
#reverse()--->returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
---------
#type(),len(),min(),max(),print()
print(sorted('Gayathri'))#returns List in ascending order
print(sorted(['code','23',34,45]))#raises error
--------
#Tuples---->Tuples are indexed,ordered,heterogenous,immutable collection
#dimentions,coordinates,database records, we prefer() for tuple notation
a = ()
print(type(a))
print(len(a))

obj = 1.2, 2.5
print(type(obj))
print(len(obj))
------
#operations---->indexing,slicing,striding,membership,merging,reptition
courses = ('PFS','JFS',('DA','DS'),'AegenticAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[3][-2:])
print(courses[-2][-2:])
#courses[2] = 23 --->typeError as tuples are immutable
courses[-1].append('codegnan')#we can make any modifications inside list
print(courses)
-------'''
#task
#create a nested tuple as above and work on slicing,striding and list function
a = ('gayathri','bhavani','DA','DS',('ABC','DEF'),'hema','manu',[10.20,30])
print(a)
print(len(a))
print(a[4][1:])#slicing
print(a[4][:1])
print(a[1:5])
print(a[::2])#striding
print(a[::-1])
a[-1].append(40)#list
print(a)


'''
print('PFS' in courses)#membership
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5)#merging
print(e)
------
#Tuples Immutable--->count(),index()
courses = ('PFS','JFS',('DA','DS'),'AegenticAI',[100,6,6])
print(courses.index('AgenticAI'))#returns first occurance
print(courses.count('Agents'))

#print(courses.sort())#AttributeError--> sort() is in Lists not in tuples
print(sorted(courses[-1]))
#print(sorted(courses))#as we have mixed type

#typecasting
d = tuple(sorted((23,21,3,4,5)))
print(d)
-------
#accept group of integers space separated
a,b = map(int,input("Enter the values").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print(a)
---------
#eval() it can take any kind of input
print('9+4')
print(eval('9+4'))

a = eval(input("enter a list:"))#in this case u can exactly enter data as
print(a)
print(type(a))
'''
#Task:take a user input as string,do this in two ways...
'''
1) give the count of each repeating charcter
Testcase 1: programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
r is repeating 2 times
index = [3,10]
r is repeating 2 times
index = [6,7]
'''
# Task: take a user input as string, do this in two ways...

s = input("Enter a string: ")

# 1) give the count of each repeating character
for ch in set(s):
    count = s.count(ch)
    if count > 1:
        print(f"{ch} is repeating {count} times")
print()

# 2) give the count of each repeating character along with their indices
for ch in set(s):
    indices = [i for i, c in enumerate(s) if c == ch]
    if len(indices) > 1:
        print(f"{ch} is repeating {len(indices)} times")
        print(f"index = {indices}")



















