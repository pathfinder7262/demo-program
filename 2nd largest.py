#2nd largest


lst = [2,4,3,8,6,0,4,7,6,2,88,6,44,3]
print( lst.sort())

lst2 = list(set(lst))  #remove duplicate
print(lst2)
print(lst[1])  #2nd smallest
print(lst2[len(lst2)-2])   #2nd largest



