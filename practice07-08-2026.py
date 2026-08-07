'''
#07-08-2026
#Write a program to calculate the inings ofa bats man,count of the boundaries,dot balls and total socre. using For loop
score = int(input("Enter the number of balls:"))
total_score = 0
for i in range(score):
    run = int(input("Enter runs:"))
    if run == 0:
        print("Dot ball")
    elif run == 6:
        print("Boundary")
    else:
        total_score = total_score + run
        print("Total_score:", total_score)

runs = list(map(int,input("Enter the score").split()))
total_score = boundaries = dotballs = 0
for i in runs:
    total_score += i
    if i == 4 or i == 6:
        boundaries += 1
    elif i == 0:
        dotballs += 1
print("boundaries:", boundaries)
print("dotballs:", dotballs)
print("total_score:",total_score)

#phone pattren unlock using while loop
pin = "1412"
max_attempts = 5
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Enter the pattren:")
    if entered_pin == pin:
        print("phone unlocked!")
        
    else:
        print("Entered pin is not valid")
        current_attempt += 1
else:
    print("Entered pin is invalid...Try again after 30 secounds...")
        
'''
# ATM pin auethentication
pin = "1979"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("log-in successful")
        
    else:
        print("Entered pin is not valid....Try again carefully")
        current_attempt += 1
else:
    print("Account Locked,Try again after 24hrs.....!")

