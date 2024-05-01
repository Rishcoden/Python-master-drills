lst = list(map(int,input("Enter the list ").split()))
target = int(input("Target:  "))
i = 0
j = 1
s = 0
t = 0
l = len(lst)
for i in range(i,l):
    for j in range(j,l):
        if lst[i]+lst[j]==target and i!=j:
           s = i
           t = j
           break
print([s,t])    
    