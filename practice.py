'''
#e-commerce product price sum from coustmers cart 
price = list(map(int,input().split(',')))
total = 0
for i in price:
        total = total + i
print(total)

#Password Analyizer and count the uppercase,lowercase,specialchar,digits in the password
Password = input("Enter the password:")
upper=lower=digit=special= 0
for ch in Password:
    if 'A'<=ch<='Z':
        upper +=1
    elif 'a'<=ch<='z':
        lower +=1
    elif '0'<=ch<='9':
        digit +=1
    else:
        special +=1
print("Upper:", upper)
print("Lower:", lower)
print("Digit:", digit)
print("Special:",special)

#extraction of 'gmail.com' from email id
email = input("Enter the E-mail:").split(',')
for mail in email:
    print(mail.split("@")[1])

#print of the movie history in serial numbers from OTT platfrom
movies = input("Enter movies names:")
count = 1
for movie in movies:
    print(count, movies)
    count += 1

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
pin = "1971"


























        
        
    
    
    
