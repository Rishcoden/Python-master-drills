'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.
For example:

    Input: "()", Output: True
    Input: "()[]{}", Output: True
    Input: "(]", Output: False
    Input: "([)]", Output: False

Solve this problem using a stack data structure.


'''
lst = []
s = input()
k = s[::-1]
lst.append(s)
max = s[0]
next_bounce = s[1]
z = 0
lenght = len(s)-1
i = 0
j = lenght
g = len(s)/2
count = 0
while(z<g):
   if ord(s[j])-2==ord(s[i]) or ord(s[j])-1==ord(s[i]):
     count = count+1
     i=i+1
     j=j-1
   else:
    if ord(max)==ord(next_bounce)-2 or ord(max)==ord(next_bounce)-1:
      for p in lst:
        lst.pop()
        
    else:
       pass
   z=z+1
if count==len(s)/2:
    lst.pop()
else:
    pass
if(lst==[]):
    print("True")
else:
    print("False")


