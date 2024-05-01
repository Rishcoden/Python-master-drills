# this function deltes duplicates from a list

'''lst = [1,4,4,3]
check = list(set(lst))
print(check)'''
# disadvantages it changes the order of the list


# method 2
lst =[1,4,4,3]
check = []
for i in lst:
    if i not in check:
        check.append(i)
print(check)