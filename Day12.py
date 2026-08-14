'''
Sequences---->strings,lists,tuples,set,frozenset
mapping--->dictionary
-----
#Sets ---> A set is a unique collection of objects, unordered, mutable, Hashing, unindexed, unique, heterogenous
#set(),{}
#a = {}
a = set()
print(type(a))
stud_ids = {123,345,345,678,145}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])--->TypeError
print(345 in stud_ids)
#print(stud_ids *2)--->TypeError
#print(stud_ids + stud_ids)#two sets cannot be merged--->TypeError

#data = {12,3,4,5,6,[12,3,4],'Gayathri'}
#print(data)#no lists inside a set (hashing technique) lists are mutable
a = {12,3,4,5,6,(12,3,4),'Gayathri'}
print(a)
print(len(a))
for i in a:
    print(i)
------

#methods on sets-->add(),update(),remove(),discard(),pop()
names = {'gayathri','siddu','prem','codegnan'}
print(len(names))
names.add('python')
print(names)
names.add('gayathri')
print(names)
#names.add('gayathri','poll')
#print(names)
names.add(('poll','java'))
print(names)
#names.add({'DA','DS'})-->TypeError
#print(names)
------

#update() we can update multiple elements(set)
da_names = {'mani','akash','sai','sonu'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))
--------
#remove(),discard(),pop(),clear()
#remove() removes an element from the set (it must be a member)
da_names = {'mani','akash','sai','sonu'}
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#keyErro-r
-----
#discard() will remove an element if its present else it ignores
da_names.discard('python')
print(da_names)
#pop(),update()
da_names = {'gayathri','siddu','prem','codegnan',('poll','java'),'mani','akash','sai','sonu'}
da_names.pop()
print(da_names)
print(da_names.pop())#it removes and returns an arbritrary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['sai','akash'])#update can take any braces as it returns the elments in the set
print(da_names)
da_names.update({'DA','DS'})
print(da_names)
-----
#copy()
d = names.copy()
print(d)
d.update({'DA','DS'})
print(d)
print(names)
'''
#Mathematical operation--->union(),intersection(),difference(),symmetric_difference()
#issubset(),issuperset(),isdisjoint()
da_23 = {12,23,34,45,23,26}
da_24 = {34,46,47,23}
'''
#event = da_23.union(da_24)
event = da_23 |(da_24) # &---> union
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & (da_24)#|-->intersection
print(common)
print(len(common))
dif = da_23.difference(da_24)
print(dif)
print(len(dif))
common = da_23.intersection_update(da_24)
print(common)#it returns None
print(da_23)#common elements are finally stored
------
#difference() removes common elements and prints rmng elements from first set 
print(da_23)
print(da_24)
#dif = da_23.difference(da_24)
#print(dif)
f = da_23 - da_24
#print(f)
#symmetric_difference()--->removes common elements and prints all rmng
#elements from 2 sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h = da_23 ^ da_24# ^---> symmetric_difference
#print(h)
------
#issubset()-->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
------
#isdisjoint() returns false for sets having common elements
print(da_23.isdisjoint(da_24))
print(da_24.isdisjoint(da_23))
'''
#length of unique students ids in a class, where user can enter first input
#we should be giving number of student_ids,he will enter student_ids

n = int(input())
std_ids = input().split()
#print(std_ids)
result = set(std_ids)
print(result)
print(len(result))
























