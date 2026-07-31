''''
#Identity operators --> checkes the identity of an object-->id()

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5==5)

a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
# As we have Lists (Mutable collection) both c and a lists will have different
#ids whereas values are same
print(c is a)#output False : here its an identity op
print(c == a)#output true : here it compares the values as a and c has the same value.sice it is coparision op
print(a is not c)
print(a is not b)

#Bitwise Operations --> we preform bitwise operations over operands
#&(and), |(or), ^(XOR), shifiting operators(<<,>>)
print(5&3)# both 5 and 3 to be converted binary and bitwise and is preformed
print(5|3)# Bitwise OR
print(5^3)# Bitwise XOR
print(5 and 3)# here and is the logical operator checks for both existances
#returns 5 in above case
print(5 or 3) # returns 3 in this case

#Leftshit Operator <<, Rightshift Operators >>
print(5<1)# False Comparision
print(5<<1)#Leftshift operation by 1 position
print(5>>1)#Rightshif operation

print(15<<2) #convert 15 to binary and perform 2 times left shifting
print(15>>2) # same 2 times right shifting

#Input Formatting --> input(), int(input()), float(input())
#we know --> single input
#2 or 3 inputs --> map
#group of integers --> List(map(int,input().split(',')))
names = input("Enter the names:").split(',')
print(names)
name1,name2 = map(str,input("Enter the friends names:").split(','))
print(name1,name2)
'''
#Tokens --> Numeric Datatypes--> operartors-->Flow of the program
#Control Block Statements--> they control the flow of the program
#when to execute, how to execute
#Conditional Statement -->if,else,elif(rely on condition to be execute)
#Repetition Statements(Loops) --> for,while

#Conditional Statements --> if usage
'''
Syntax:

if <condition>:
    statement(s)...
    .....

#age = 15
age = int(input("Enter your age:"))
if age>=18:
    print('your age is:',age)

age = int(input("Enter the age:"))
if age>= 18 and age in [19,20,22]:
    print('your age is:',age)
print(age)

#else keyword --> if-else

else:
    statement(s)...

if-else usage as below:

if <condition>:
    statements(s)...
    .....
else:
    satements(s)....
    .....

#Vote Elgibility --> To check his/her voter eligibilty and give access...
age = int(input("Enter the age:"))
if age>=18:
    print("you have voter eligibilty and age is",age)
    print("Access Granted")
else:
    age = 18-age
    #print("you dont have eligibilty as your age is",age,"years")
    print("you need to wait for",age,"more years")

age = int(input("Enter the age:"))
if age >0:
    if age>=18:
        print("you have voter eligibilty and age is",age)
        print("Access Granted")
    else:
        age = 18-age
        #print("you dont have eligibilty as your age is",age,"years")
        print("you need to wait for",age,"more years")
else:
    print("you have entered -ve values/zero enter only +ve")

Task : Student marks and grade analayzer
90 - 100 --> "A"
80 - 89 --> "B"
70 - 79 --> "C"
60 - 69 --> "D"
>60 --> Fail
#also -ve cases should not be allowed and marks shloudn't be in -ve values
'''
marks = int(input("Enter the students marks:"))
if marks >= 0:
    if marks <= 100:
        if marks >=90:
            print ("Grade A")
        else:
            if marks >= 80:
                print("Grade B")
            else:
                if marks >= 70:
                    print("Grade C")
                else:
                    if marks >= 60:
                        print("Grade D")
                    else:
                        print("Result: Fail")
else:
    print("Invaild! Marks should not be greater than 100")
    print("Invaild! Marks should not be a negative")

        

































