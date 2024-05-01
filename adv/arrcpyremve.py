

def miniMaxSum(arr):
    sample = []
    count = 0
    for i in arr:
        a = arr.copy()
        a.remove(i)
        count = sum(a)
        sample.append(count)
    m = max(sample)
    l = min(sample)
    print(l,m)
    



    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
