##n=3
##for i in range(1,n+1):
##    if(n!=0):
##        n = n-1
##    print(n)
##    n=n-1
##"""    

"""
a = 8
b = 9

def fundemo(a ,b):
    if(a<b):
        return fundemo(b,a)    #8,9 #True
    elif(b!=0):
        return(a+fundemo(a,b-1))
    else:
        return 0

result=fundemo(8,9)
print(result)
"""
'''
def fundivi(a):
    ec = 0
    nr=a
    while(nr):
        digit =nr%10
        if(digit != 0 and n % digit ==0):
            ec=ec+1
        else:
            nr=nr/10
        break
    return ec

print(fundivi(2630))
'''
'''
for i in (range(0,11)):
    if i ==5:
        break
    else:
        print(i)

for i in "chetanchaudhari":
    if i == "u":
        break
    else:
        print(i)

while(10):
    print("cc")
    if 
    break

'''
'''
for i in "ChetanChaudhari":
    if i == "q" and i =="p":
        continue
    else:
        print(i)

lst = [10,-47,63,-65,32,-65,-98,-54,43,34,23]
lst2=[]
lst2=lst.copy()
for i in lst:
    if i <= 0:
        continue
    else:
        print(i)
        
        
a = int(input("Enter the number: "))
if (a<=0):
    print("Invalide number: ")
else:
    i = 1
    while(i<=a):
        print(i)
        i = i+1
=======================================================
#table of 1 to n numbers:
a = int(input("Enter the Number: "))
if a <= 0:
    print("Invalid number: ")
else:
    for i in range(1,a+1):
        print("Table of  ",i," is:")
        for j in range(1,11):
            print("table: ",j * i)
=======================================================
#Get Number From User Put It Into A List And Show List As Well As Table.
sol = int(input("Enter the size of list: "))
if sol <= 0:
    print("Invalid")
else:
    lst = []
    for i in range(1,sol+1):
        ele = float(input("Enter the Element: "))
        lst.append(ele)

print(lst)
for i in lst
=======================================================
##program for cal sum of two numbers using functions taking i/p from user
def add(a,b):
    print("line112" )
    c = a+b
    return c

a= int(input("Enter the Number: "))
b= int(input("Enter the Number: "))
print(add(a,b))

#Swap Number:
def swap(a,b):
    print("This function is Used For Swappig Number: ")
    a = a^b
    b =a^b
    a =a^b
    return a,b

a = int(input("Enter the number: "))
b = int(input("Enter the Number: "))
print(swap(a,b))
=======================================================
#test whether number +ve or -ve
def numpn(n):
    if n >0:
        return ("Number is +ve: ")
    elif (n<0):
        return ("Number is -ve")

    else:
        return ("Number is Zero")

try:
    print(numpn(+210))       
except (TypeError):
    print("Please enter the Digit Only")
=======================================================
#Factorial Number:
def fact(n=int(input("Enter the number: "))):
    
    dig = 1
    while(n>=1):
        dig = n*dig
        n = n-1
    return dig


print(fact())
print(fact())
print(fact())


lst1 = [1,2,3,4,5]
lst2=[6,7,8,9,10]
lst3 = lst1 + lst2
lst1.clear()
lst2.clear()
print("lst1: ",lst1)
print("Lst3= ",lst3)

for i in lst3:
    if i % 2== 0:
        lst1.append(i)
    else:
        lst2.append(i)

print("Final output:")
print("lst1 of even: ",lst1)
print("lst2 of odd: ",lst2)
=======================================================
#prime number
def prime(n):
    x = True
    for i in range(2,n):
        if n%i == 0:
            x = True
            break
        else:
            x = False
    return x
re = prime(4)
if re == False:
    print("Prime")
else:
    print("Not Prime")
=======================================================
#program to add 2 complex number
def addcomplex(a,b):
    c = a+b
    return c
print(addcomplex(2+3j,6+4j))
=======================================================
#convert multiple number into decimal
def converno(a,b,c):
    aa = int(a)
    bb = int(b)
    cc = int(c)
    return aa,bb,cc

re= converno(0o17,0B1110010,0x1c2)
for i in re:
    print(i)
=======================================================

#Default parameter 1st Ex.

def car(clr,sttr,ab,com="Hondai"):
    print("{},{},{},{}".format(clr,sttr,ab,com))

car("Red",5,2)
car("Red-Black",4,1)
car("Red-pink",7,4)
car("Red-yellow",8,6)

#Default parameter 1st Ex.

def sumop(a=10,b=20):
	print("{} + {}={}".format(a,b,a+b))

#main program
sumop()
sumop(100)
sumop(1000,2000);
sumop(12.34)
sumop(-12,-34.12)


#Default parameter 2nd Ex.
def  dispempinfo(eno,ename,esal,dsg="SE",cname="IBM"):
	print("{}\t{}\t{}\t{}\t{}".format(eno,ename,esal,dsg,cname))

#main program
print("-"*50)
print("Employee Information")
print("-"*50)
dispempinfo(10,"Rasmi",3.4)	  #function call
dispempinfo(20,"Sonali",3.6)	  #function call
dispempinfo(30,"Laxmi",3.8)	  #function call
dispempinfo(40,"Priti",3.7)	  #function call
dispempinfo(50,"SSree",13.7, "TL")	  #function call
dispempinfo(60,"Arthi",4.7)	  #function call
dispempinfo(70,"shrusti",5.7)	  #function call
dispempinfo(80,"Chitra",6.7,"DBA", "Infosys")	  #function call
print("-"*50)

========================================================
#key Word parameter

def car(clr,sttr,ab,com="Hondai"):
    print("{},{},{},{}".format(clr,sttr,ab,com))

car("Red",5,2)
car("Red-Black",4,1)
car("Red-pink",7,4)
car("Red-yellow",8,6)
========================================================
#keyword parameter

def empdtl(ename,eid,egender,esal,edesig,ecom="honda"):
    print("{}\t{}\t{}\t{}\t{}\t{}\t".format(ename,eid,egender,esal,edesig,ecom))

empdtl("cc",1,"M",45000.00,"Devloper","Shine")
empdtl("cc",egender="F",edesig="Tester",esal=14000.00,eid=2)
empdtl(ecom="Hero",edesig="Helper",esal=21000.00,egender="M",eid=4,ename="Rohit")
empdtl(ename="pp",eid=5,egender="M",esal=40322.32,edesig="Coder",ecom="Python")
========================================================
'''
def   disp(a):
    print(a)
def  disp(a,b):
    print("{}\t{}".format(a,b))
def  disp(a,b,c):
    print("{}\t{}\t{}".format(a,b,c))

disp(10)...1
disp(10,20)...2
disp(10,20,30)...3

In The above function only last function will execute i.e 3









