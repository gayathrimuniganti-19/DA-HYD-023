'''
Control Statements --> control of Flow of excution of the program
                    --> Conditional Statements --> if, elif,else...
                    --> Repetition Statements(Loops) --> for, while,(for with else)(while with else)
--> Jumping Statements--> break,continue,pass
'''
#Loops Lopps are helpful for repitition(Automative tasks)
#Syntax for (for keyword):
#for keyword will be helpful to iterate over a sequnce / range
'''
for you have a temp variable(<temp_var>) sequence/range:
    statements(s)....
    ......

#range(stop) --->default 0 ends at stop-1
#range(start, stop, step)
#by default ranges picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations

for i in range (1, 10):
    print(f'Value of i is --->{i}')
    
for i in range (1, 10):
    #if i > 5:
        #print(f'Value of i is --->{i}')
#Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print(f' Final Value i is ---> {i}')

#range(Start, stop, step) --->here step--> intervel...
for i in range(1,10,3):
    print(i)
    print("Done")

for i in range(10,0,-2):
    print(i)

for i in range(-10,0,1):
    print(i)

#[] --> we generally in lists
names = ['Gayathri','manasa','hema']
for i in names:
    print(i)
    
#[] --> we generally use in lists
names = ['Gayathri','manasa','hema']
print(len(names))#len(obj)---> returns the number of items in container
for name in names:
    #print(name)
   # print(f'Student Name is {name}')
    if name == "Gayathri":
        print(f'Student name is {name}')

#Task
#Calculate the sum of First 10 numbers
# first understand you input --> range(11) -->10 numbers
#second understand your output --> sum(number)
#thrid we need to map the logic
result = 0 # target variable
for i in range(11):
    #print(i)
    #print(f'result is {i+i}')
    result = result + i # result += i
    print(f'Now the result is {result}')
print(f'Sum of 10 numbers is {result}')

#the sum 10 even numbers
result = 0 
for i in range(21):
    if i %2 == 0:
        result = result + i
print(f'Sum of 10 even numbers is {result}')

'''
#Understand the loops usage with Fitness Streak example
#work_out --> 1,work_ot_missed --> 0
work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + day
        if current_streak > longest_streak :
            longest_streak = current_streak
    else:
        current_streak = 0 #streak break
print(f'longest streak is {longest_streak}')

































    
