t = int(input())
count = 0
for i in range(t):
    lst = list(map(int,input().split()))
    summation = sum(lst)
    if (summation3>=2):
        count+=1
print(count)