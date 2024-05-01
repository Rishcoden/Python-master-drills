def seperateStone(n,k,arr):
      w = 0
      b = 0
      countw = 0
      countb = 0
      for i in arr:
        if i==0:
            w = w+1
        elif i==1:
            b = b+1
      for i in range(1,w+1,k):
          countw = countw+1
      for i in range(1,b+1,k):
        countb = countb+1
      return countw+countb  



n = int(input("Enter the value of n "))
arr = list(map(int,input("Enter the array ").split()))
k = int(input("Enter the value of k "))
output = seperateStone(n,k,arr)
print(output)