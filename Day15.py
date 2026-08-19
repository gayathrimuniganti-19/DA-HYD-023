'''
Functions-->Variable length arguments(*args)
         -->Keyword variable length arguments(**kwargs)
Variable length arguments--->The number of positional arguments are not limmited
we can pass any number of arguments, but we need to use the * respresentation data stored in tuple
--------
def sample(*args):
    """Sample demo for *args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,5,6)#any number
sample('codegnan','Gayathri',22)
details = [23,24,34,45]
sample(details)#passing a collection
sample(*details)#unpacking values from collection
---------
#'*' is used for unpacking the values from a collection
a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c= 'python','codegnan',24,45,9.7,'data'
#a,b,*c= 'python','codegnan',24,45,9.7,'data'
a,b,*c = 34,'codegnan'
print(a)
print(b)
print(c)
c.extend([24,25,2,6])
print(c)
---------
#Task: We wanted to calculate the sum of given objects using functions
def add(*a):
    """"Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0
    for i in a:
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            #print(i)
            result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4,5.6))
#add(3,4,5,'poll','dear',4.5)hence its the breaks the sum since it contines strings
#print(add(3,4,5,5.5,2+4j,56.'code',23))
print(add(3,4,5,'poll','dear',4.5))
b = list(map(int,input("Enter the values:").split(',')))
#print(add(*b))#here  '*' is used to unpack the values from collection
print(b)
print(*b)#it returns each value sde by side
for i in b:
    print(i,end='') #it does the same process here as the "*" do
--------
#Keyword vaiable length arguments--->we can pass any number of keyword arguments we use ** representation
data stores in dictionary

def details(**kwargs):
    """Üsage of *kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()#returns empty dictionary
#details(2,3,4,5)#TypeError
details(name='codegnan',place='HYD',batch='da')
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''
#now let us include both of them into a function
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

#done






































