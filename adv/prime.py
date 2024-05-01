p = True
n = int(input("Enter a number to find it is prime or not"))
for i in range(2,n):
    if(n%i==0):
        p = False
        break
if p == False:
    print("It is not a prime")
else:
    print("It is a prime")