
n,m = map(int,input().split())

for i in range(1,n+1):
    if i**2>=n:
        square = i
        break 
if square**2 > n:
    square = square-1
a = square
b = n - square**2 
if (a**2+b==n) and (a+b**2==m):
    print('1')
else:
    print('0')
    



