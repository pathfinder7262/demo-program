#program for check the str has duplicate element or not

str2 = "chetann"
flag = False
'''
for i in str2:
    if (str2.count(i) != 2):
        flag = False
    else:
        flag = True
        break

if flag == True:
    print("Got it")
else:
    print("not")
        
'''

lst1 = []
for i in str2:
    lst1.append(str2.count(i))

for j in lst1:
    if j == 2:
       print("got it") 
    else:
        print("not")

'''+ 
if any("o" in i for i in str2):
    print("mil gya")
else:
    print("Not")
'''
