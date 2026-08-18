'''
Tokens,datatypes-->control flow statements-->if,elif,else,for,while,break,continue..

procedure oriented programming
Functions-->A function is a block of code which performs a specific task
its reusable block of code where we define using 'def' keyword
Advantages--> code reusability,code maintainability,ease of debuggind,avoiding code duplication, modularity
----
syntax:
def fname(parameters): Function def'n
    """Doc String""" #it is the discription
    statements(s)...    Function body
    return value(s)...
fname(args)             Function call

-----
#To perform some of given objects
def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,4))#Addition
print(add('code','gnan'))#concatenation
print(add([12,5],[12,34]))#merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects without retrun"""
    print(a+b)
add('code','gnan')
print(add(12,-34))#it returns result along with None
-------
name,age,salary = 'gayathri',22,500000
#usage of return
def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+45+34
    return  #it returns None as output
print(details())
------
There are 5types of arguments:
--->Positional Arguments
--->Default arguments
--->Keyword arguments
---->variable length arguments(*args)
---->keyword variable length arguments(**kwargs)
--------
#Positional Arguments--->Number of args in function defn should match with function call(order has to be maintained)
#print(len(123,234)) thi is as per built-in len(obj) will accept one arguments

def details(name,place):
    """ To store the details"""
    #name = "Codegnan"
    #place = "HYD"
    #return name,place
    print(f'Name is {name}')
    print(f'Place is {place}')
#print(details("Gayathri","Codegnan"))
#print(details("Sai","Vizag"))
#print(details("Vizag","shyam",32))#raises TypeError as only 2 arguments to
c,d = map(str,input("enter the values").split(','))
details(c,d)
-------
#def grocery(item,price=35):
#def grocery(item="Cheese",price=100): #we can also make all args as default
#def grocery(item="Burger",price):#non default always follows default
    """Usage of default arguments"""
    print(f'The Item is {item} and Price is {price}')
grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread")#by default we have given price as 35
grocery("Bread",45)
grocery()# as both item and price as default arguments
'''
#Keyword arguments---> Whenever we want to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}, works in {place}')
employee("Gayathri",40000,"Data Analyst")
#employee(25000,"frontdesk","asha")
employee(salary=25000,role="frontdesk",name="Asha")
employee("Akash",250000,"IT","Amazon")


































