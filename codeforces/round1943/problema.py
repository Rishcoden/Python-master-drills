t=1 
n = int(input(""))
while(t<=n):
 l=int(input())
 lsta = list(map(int,input().split()))
 lst = sorted(lsta)
 c = []
 mex=[]
 l = len(lst)
 for i in range(0,l,2):
    c.append(lst[i])
 for k in range(0,len(c)+1):
    if k not in c:
        mex.append(k)
 print(min(mex))
 t=t+1
 