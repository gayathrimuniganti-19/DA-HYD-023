'''
Functions--->arguments usgae(Variable length arguments)
        --->Keyword variable length argumrnts(**kwargs)
EXCEPTION HANDLING / Scope of variables/Built-in Functions
Exception handling---> It is a mechanism that hepls to respond or make the flow of execution in normal way, without this errors will occur and disrup the flow of program
Common Exceptions--->ValueError,TypeError,IndexError,AttributeError,ZeroDivisionError...

Syntax:

try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective of try/except...
-----------
#basic exception handling
try:
    #a = 10
    a = int(input("Enter the value:"))
    result = 20/a
    print(result)
    #print(resul)#check for NameError
#except Exception as e:
    #print(e)#it returns the msg instead of errors
except ValueError:
    print(f'Invaild entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properly')
--------
#Similarly if we want to check others Errors-->IndexError,AttributeError
#Multiple Exception Handling
try:
    a = [10,20,30]
    a.apped(24)
    print(a[5])
#except Exception as e:
    #print(e)
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')

def sample(*a,**b):
    """Üsage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    print(result)
    for key,value in b.items():
        print(f'Key is {key}')
        print(f'Value is {value}')
    return result
sample(2,4,5,'police','codegnan',3.5,
       name="Codegnan",
       place ="hyd",
       batch = "da23")
------
#handling exceptions at a time
try:
    a = [10,20,30]
    a.apped(24)
    print(a[5])
#except Exception as e:
    #print(e)
except (IndexError, AttributeError) as e:
    print(e)
    a = list(map(int,input("Enter:").split(',')))
    print(a)
----------
#BMI ---> bmi = (weight) / ((height)**2)
#Feet-->12 inches--> 1 inch -> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in meters:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break #stops the flow of execution of program
            #continue #skips the current iteration and proceed for rmng iteration
            #print("Bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only,height also as number')
bmi = ((weight)/(height))
print(bmi)
--------
#Use Exception Handling along with Jumping statement in Functions BMI Task

--------
#Scope of Variables-->Scope is basically the region/area where it is accessible
#Local Scope, Global Scope
#Global Keyword, Enclosing Scope(nested functions non local keyword)

#Local scope--->variables defined inside the function accessible inside

def display():
    """Üsage of Local Scope"""
    name="Codegnan"#local variable
    print(name)
display()
#print(name) #it rises NameError
------
#Global Scope(variables)-->Defined outside and can be accessible anywhere in the script
place = "Hyderabad"
def display():
    """Üsage of local&Global Scope"""
    name = "Codegnan"#local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place) 
------
#Modifying global variable inside the function the function and accessible outside the function
count = 20
def data():
    """Üsage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
---------
#local variable has high priority over global variable
count = 20
def data():
    """Priority of local vs global variable"""
    count = 5 #local variable
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
------
#Enclosing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''
#built-in functions-->vairable builtinscope
len = 65
print(len+4)
print(len('codegnan'))#typeError--->never ever use built-in function as identifiers
#it is acting as vairable


































