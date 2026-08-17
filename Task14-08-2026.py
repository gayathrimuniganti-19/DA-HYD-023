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
numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print("Ascending:", numbers)
numbers.reverse()
print("Descending:", numbers)
print("Numbers:")
for n in numbers:
    print(n)
search = int(input("Enter number to search: "))
if search in numbers:
    print("Number found")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("Number not found")
print("Smallest:", min(numbers))
print("Largest:", max(numbers))
print("Total:", sum(numbers))
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
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
print("Union:", python_students.union(da_students))
print("Intersection:", python_students.intersection(da_students))
print("Only Python:", python_students.difference(da_students))
print("Only one course:", python_students.symmetric_difference(da_students))
if da_students.issubset(python_students):
    print("DA is a subset of Python")
else:
    print("DA is not a subset of Python")
if python_students.issuperset(da_students):
    print("Python is a superset of DA")
else:
    print("Python is not a superset of DA")
if python_students.isdisjoint(da_students):
    print("Students are disjoint")
else:
    print("Students are not disjoint")
print("Students learning both:")
for student in python_students.intersection(da_students):
    print(student)
































    
