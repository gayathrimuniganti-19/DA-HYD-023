#Perfect number
n = int(input("Enter the perfect number:"))
count = 0
for i in range(1,n):
    if n % i == 0:
        count += i
if count == 0:
    print( "it is perfect number")
else:
    print("not a perfect number")
        
