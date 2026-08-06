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
'''
#print of the movie history in serial numbers from OTT platfrom
movies = input("Enter movies names:")
for movie in movies:
    
