'''A permutation is a sequence of integers p1, p2, ..., pn, consisting of n distinct positive integers, each of them doesn't exceed n. Let's denote the i-th element of permutation p as pi. We'll call number n the size of permutation p1, p2, ..., pn.

Nickolas adores permutations. He likes some permutations more than the others. He calls such permutations perfect. A perfect permutation is such permutation p that for any i (1 ≤ i ≤ n) (n is the permutation size) the following equations hold ppi = i and pi ≠ i. Nickolas asks you to print any perfect permutation of size n for the given n.

Input
A single line contains a single integer n (1 ≤ n ≤ 100) — the permutation size.

Output
If a perfect permutation of size n doesn't exist, print a single integer -1. Otherwise print n distinct integers from 1 to n, p1, p2, ..., pn — permutation p, that is perfect. Separate printed numbers by whitespaces.

Examples
inputCopy
1
outputCopy
-1
inputCopy
2
outputCopy
2 1 
inputCopy
4
outputCopy
2 1 4 3 
'''

a = int(input())

mylst = []

for i in range(1,a+1):
    mylst.append(i)
mylst.reverse()
if a==1:
    print("-1")
else:
 print(mylst)
