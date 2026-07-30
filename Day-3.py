#numeric Datatype --> int,float,complex along with boolean

#Input formatting --> Accepting input from user -->input()

#Accepting input from user
# by defulat input() accepts any input-->str
#int(input()) --> will only accept integers
'''
age = int(input ('Enter the age:'))
print(age)
print(type(age))

age = float(input ('Enter the age:'))
print(age)
print(type(age))


#Accepting string input from user

name = input("Enter the name:")
print(name)
print(type(name))

#Accept group of values

marks = int(input("Enter the marks")).split()
print(marks)


a = input().split() # By default split() has space
print(a)

#space separeated values
a = input().split() #now you enter spaces in output
print(a)
#comma separated values
a = input("Enter the values:").split(',')
print(a)

a = input("Enter the values:").split('*')
print(a)

#List of integers
marks = list(map(int, input('Enter the values').split(',')))
print(marks)
#here the map states the values and list store the values and produce the in list from

#now we want to accept 2 values from user
age,salary = map(int,input('Enter the values').split(','))
print(age)
print(salary)

#Single input ---> int(input())
#two inputs --->a,b = map(int,input().split(','))
#any number result as list --> a = list(map(int,input().split(',)')

#group of float values
age,salary = map(float,input('Enter the values').split(','))
print(age)
print(salary)

#float of integers
a = list(map(float,input('Enter the values').split(',')))
print(a)

#Accepting input from user --> int,float -->input formatting

#Operators --> operators perfrom operations between values (operands)
#they are 7 types --> Arithemetic,Assignment,Comparsions(Relationship)
#Membership,Identity,Logical,Bitwise
#Arithemetic Operators
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#Float value
print(5//3)# '//' are used to returns the quotient value
print(5%3)# '%' is used to returns the reminder
print(5**3)# '**' is a power (exponential)
#Floor Division ( integer division)--> returns quotient


#Task --->Accept integer input as length, breadth ---> find the area of rectangle
#Area = length * breadth
length = int(input("ënter the length:"))
breadth = int(input("enter the breadth:"))
area = (length * breadth)
print(area)
#OR
length, breadth = map(int,input("Enter the values:").split(','))
area = length * breadth
print(area)
'''
#Assignment operators -->assign the values
# =, +=, -=
a = 50
print(a)
#updating the value of a
a = a+10 #a+=5
print(a)

b = 35
b += a #b=b+a
print(b)

b = 35
b -= 5 #b=b-5
print(b)

#Task : *=, /=, //=, %=, **=,
b = 35
b *= 5
print(b)

b = 35
b /= a
print(b)

c = 67
c //= b
print(c)

e = 80
e %= 2
print(e)

f = 90
f **= 2
print(f)
'''
#Comparision Operatons -->we compare the values --> gives boolean output
# ==(equal to , !=(not equal to), <(less than equal to), >(greater than))
# <= and >=

age =25
print(age == 25)#returns the boolean output
print(age != 35)
print(age < 32)
print(age > 26)
print(age<=32)
print(age>=32)
print(-5 < -1)

#Membership Operators --> in, not in
# Its checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)
print(45 in marks)
#print(35 in 355) ---> TypeError
print(25 not in marks)
print(45 not in marks)

print('code' in 'codegnan')
print('#' in '^%&#&')

#Logical Operators --> logical decision making ---> and,or,not
#and -->all conditions to satisfied
#or -->any one condition to be satisfied

a = (25 in [25,45,65]) and 45>56
print(a)
b = 45>56 or 25<=45
print(b)
c = not(True)
print(c)

#Identity Operators --> check for identity of an object--> id()
a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
'''
'''
a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
'''













