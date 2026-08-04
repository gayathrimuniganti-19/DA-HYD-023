'''
Usage of else with for --> the else keyword will only be executed when the loop is completely done without any break

work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + day
        if current_streak > longest_streak :
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0 #streak break
else:
    print(f'longest streak is {longest_streak}')
#In this case when the entire loop execution is done we get result of else block

#same program with break usage
work_log = [0,1,1,1,0,1,0]
longest_streak = 0 #target variable
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + day
        if current_streak > longest_streak :
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0 #streak break
else:
    print(f'longest streak is {longest_streak}')
print("Execution done")

#for-else with notification scenario
notifications = [0,0,0,1,0]
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print("All Caught Up!")
    
# try to take notifications from user ---> list of integers
notifications = list(map(int,input("Enter the values --> 0 or 1:").split(',')))
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print("All Caught Up!")
'''

#while -->ir relies on condition, it will be completely executed until the condition is satisified..
'''
Syntax <condition>:
        ........
        .....

while True:
     print("Yes")# It runs an infinite loop we need to press Ctrl+C(keyboard interrup)
     
i = 0#Initialised statement
while i<=10:
    print(i)
    i=i+1 #counter

#Get the counter from 10 - 1
i = 10 
while i >= 1:
    print(i)
    i = i - 1#decrement i-=1

i = 0
while i<=10:
    print(10-i)
    i = i+1
'''

#banking scenario --> PIN Authentication if more than 3 attempts
#Account Locked..

pin = "1214"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Eneter the ATM PIN:")
    if entered_pin == pin:
        print("Log in Successful")
        break
        #continue -->It holds for this condition and skips to the next part 
    else:
        print("Entered PIN is Worng...Try again carefully")
        current_attempt +=1
else:
    print("Account Locked, Try after 24hrs...")

























    
