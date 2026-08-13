'''
Sequences---> Strings,Lists,Tuples,Sets
Mapping --> Dictionary

#Lists---> Collection of heterogenous elements(items)
#List--> indexed,ordered,mutable,heterogenous,we use [] to store the data
marks = [35,25,21,45,12,48]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#operations:indexing,slicing,striding,membership,merging,repetation
-------

#nested lists--> a list inside another list
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0] [:4])#it returns Code
print(names[0] [4:])
#get the output as Cdga
print(names [0] [::2])
names[0] = names[0] [::-1]#it reverse the string
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
#indexing,slicing-->mutable
names[2] = 'python'
print(names)
#By indexing if we change the elements, length of collection will remain same
names[4] = ['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4][0][4:])
print(names[3][1:3])
print(names[4][1:4])
names[2:4] = 'Gayathri','sai','perm','manu'
print(names)#In slicing whatever elements we pass as per the logic lenght kepps on increas
names[3:6:2] = 'Python','java'
print(names)
'''
#Task
#create a nested list with strings,lists and work on indexing,slicing,striding
#added advantage if u could add string functions also to it

#Lists Functions-->append(),insert(),extend(),pop(),remove(),clear(),index(),count(),copy(),sort(),reverse()
names = ['Codegnan','Gayathri']
#append()--->inserts single element to the end of the list
names.append('Data')
#print(names)
#name.append('analysis','agents')-->TypeError
names.append(['Analysis','Agents'])
print(names)
#append() will always increment the length of list by 1
#print(names[3])
#names[3].append('Chatgpt')
#print(names)
#print(names[3].append('Chatgpt'))#it returns None as append is applicable
#on list not print
#print(names)
'''
-----
#extend()--->inserts multiple elements to the end of list
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,25,15,64])
print(names)
#names.extend(35,45)---->TypeError
#print(names)
-----
#insert(index,object) -->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'Java')
print(names)
#names.insert([1:4],['a','b']) ---->SyntaxError
#print(names)
names.insert(-1,'AAA')
print(names)
--------
#pop(),remove(),clear()
#pop() by default last,else given index
print(names.pop())
print(names)
names.pop(2)
print(names)
'''
'''
#remove() we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.remove(14)#it raises ValueError

del names[1:3]#del keyword will apply permanent changes
print(names)
names.clear()#clear() will remove all elements and returns empty list
print(names)
#Task
#data = ['codegnan','gayathri','python','java']#input
#output should be as follows
0 : codegnan
1 : gayathri
2 : python
3 : java
'''
data = ['codegnan','gayathri','python','java']
for i in range(len(data)):
    print(f'{i} = (data[i])')

















