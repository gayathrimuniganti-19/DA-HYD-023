'''
Tokens --> variables, punctuators

Variables --> named memory location, its a placholder for data
#Rules are to be followed

#Multiassignment of variables

name,age,place = 'Gayathri muniganti',22,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')#sep(seprate) is refers to seprating
print(name,age,place,sep='------->')
'''
'''
#a,b = 2,3,5 # this statment generates a value error where there are too many values to unpack

#Reassingning variables

name = 'Gayathri'
a,b = 45,1.5
print(a,b)
a,b = b,a#this is the swapping is called reassingning 
print(a,b,sep=',')

#a,b = b,c #nameerror as c is not defined
#print(a,b)

#Deleting the variables --> del(keyword)
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators --> []this is used for list notation,()this is used for tuples,{}this is used for dictionaies and sets.
name = "Gayathri";age = 7;course ='Data analysis'#;here the semicolon is used to seprate the variables.
print(name,age,course)
'''
'''
#Datatypes --> numeric (int,float,complex--imagenary numbers),boolean,None,
             #--->Sequences(lists, tuples,sets,strings,frozensets,mappings(dict))

#Numeric type -->int,float,complex
#int datatype --> it defines the quantity ex:age...
age = 22
print(age)
print(type(age)) #type -->it returns the datatype of an object

print(type(234))
'''
'''
#quantity = 03 # here the 0 is not allowed because integer doesnot start with 0
#print(quantity)

#Float Datatype -->ex: temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))
'''
'''
#Complex -->combination of real and imaginary
#2i = 5 here the 2i is not defined as variable
i2 = 4
data = 5 + i2
print(data)

data =5+2j#j is imag representation
print(data)
print(type(data))
'''
'''
#Boolean --->True / False these are used in conditional

valid = True
print(type(valid))

error = False
print(type(error))

#Typecasting --> it is the process of converting one type into another type
#Python by default follows Implicit Type(we need not mention the datattype)

#We will go for Explicit coversion

# Every built-in datatype is a built-in function
int,float,complex,bool

#Typecating -->int -->float,complex,bool

age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)
'''
'''
#Float --->Typecasting

age = 35.45
print(type(age))
b = int(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)
##second ex
price = 750.45
print(type(price))
b = int(price)
print(b)
c = complex(price)
print(c)
d = bool(price)
print(d)
e = bool(0)
print(e)
## boolean of anything is True and nothing is Flase
'''
'''
#Complex --> Typecasting --> int, float, bool
data = 2 + 5j
print(type(data))
#b=int(data) #typeError
#print(data)
#c=float(data)
#print(c)
# in typecasting the complex can not be an intger and float
d = bool(data)
print(d)
print(type(d))
d=5+4.5
print(d)
'''
'''
# conversion of int float and bool
e = int(float(bool(45)))
print(e)

f = bool(int(float(25)))
print(f)

g =float(bool(int(10)))
print(g)
'''
f = 45 + 2.5 + 2 + 3j + False
print(f)

h = 76 + 45.6 + 56+ 9j + True
print(h)

j = 65 - 76 - 10j - 12 - False
print(j)














