str1  = "asdfsd kjhjh"
lst2=[]
for i in str1:
    if  str1.count(i) == 1:
        lst2.append(i)
    else:
        continue

print(len(lst2))
