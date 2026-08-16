'''
#Students marks manager
marks = []
for i in range(3):
    mark = int(input("Enter the mark:"))
    marks.append(mark)
print("original marks:", marks)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
    print("75 removed")
removed_mark = marks.pop()
print("removed final mark:",removed_mark)
print("Final marks:", marks)
print("Number of marks:",len(marks))
------
#Number List Analyser
numbers = [20,10,30,20,40,20]
numbers.sort()
print("Ascending:", numbers)
numbers.reverse()
print("Descending:", numbers)
search = int(input("Enter number to search:"))
if search in numbers:
    print('count:',numbers.count(search))
    print('First index:',numbers.index(search))
else:
    print("Number not found")
print("Smallest value:",min(numbers))
print("Largest value:",max(numbers))
print("Total no.of numbers:",sum(numbers))
-----
#Even and Odd Number Separator
num = [5,10,15,20,25,30,35,40]
even=[]
odd=[]
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("Odd numbers:",odd)
print("First three values:",num[:3])
print("Last three values:",num[-3:])
backup = num.copy()
num.clear()
print("Original list after clear:",num)
print("Backup list:",backup)
------
#Unique Name Manager
names = ['Asha','Rahul','Asha','John','Rahul']
unique_names = set(names)
print('Unique names:', unique_names)
unique_names.add('Meera')
print(unique_names)
unique_names.update(['Priya','Arjun'])
print(unique_names)
if "John" in unique_names:
    unique_names.remove('John')
    print('John is removed')
unique_names.discard('David')
for name in unique_names:
    print(name)
------
'''
#Course Student Comparison
python_students = {'Asha','Rahul','John','Meera'}
da_students = {'Rahul','Meera','Arun'}
print('both courses:',python_students | da_students)
print('both courses students:',python_students & da_students)
print('only python:', python_students - da_students)
print('only one course:', python_students ^ da_students)
print('DA subset of python:',da_students.issubset(python_students))
print('python superset of DA:', python_students.issuperset(da_students))
print('Disjoint:', python_students.isdisjoint(da_students))
print('common students:')
for student in python_students & da_students:
    print(student)
































    
