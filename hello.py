'''
def prim(m):
    if m > 1:
        for i in range(2,(m//2+1)):
            if(m%i) == 0:
                print("Not prime")
                break
            else:
                print("prime number")
        

prim(11)
def fibb(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(3,n+1):
        c = a+b
        a = b
        b = c
        
        print(c)

fibb(10)
        
    
def sq(n):
    def innerfun()



https://join.skype.com/vqlyXCBSGNev
https://join.skype.com/urAMHVvDPbqo


#saperate str and

str11 = "asddf324fds"
for i in str11:
    if  i.isalpha():
        print(i,end="")
    else:
        continue

#count aplha and digit:
str11 = "asddf324fds"
alctn = 0
digcnt = 0
for i in str11:
    if  i.isalpha():
        alctn = alctn +1
    else:
        digcnt = digcnt + 1

print("Alphabates: ",alctn)
print("Digits: ",digcnt)


#Reguler Expression:
import re
st = "asdfGHJ:{#@K123454"


res = re.finditer("[a-z]",st)
for i in res:
    print(i)

res = re.finditer("[^a-z]",st)
for i in res:
    print(i)

res = re.finditer("[A-Z]",st)
for i in res:
    print(i)

res = re.finditer("[^A-Z]",st)
for i in res:
    print(i)

res = re.finditer("[0-9]",st)
for i in res:
    print(i)

res = re.finditer("[^0-9]",st)
for i in res:
    print(i)
#==========
st = "asdfGH J:{#@K1   23454"
res = re.finditer("[^a-zA-Z0-9]",st)
for i in res:
    print(i)


textdata="Ramu got 56 marks and whose mail id is ramu.ibm@ibm.com ,Raju got 66 marks and whose mail id is raju.tcs@tcs.com , Pujitha got 99marks and whose mail id is puji.wipro@wipro.com , Arien got 88 and whosemail id is arien.paypal@paypal.com , Bharath got 88 marks and whose mail idis bharath.google@google.com , Rasmi got 78 marks and whose mail id israasmi123.ge@ge.net , Rossum got 77 marks and whose mail id isrossum4.psf@psf.org.net and Gosling got 44 and whose mail id isgosling.sun@sun.com and kvr got 11 marks and whose mail id iskvr.igatemnc@igate.com and Mayur got 99 and whose mail id is mayur2.igatemnc@igate.com and Gauravj got 69 and whose mail id is gaurav.apple@apple.com"
mails=re.findall("\S+@\S+",textdata)
print("-"*50)
print("All Student Mails Ids")
print("-"*50)
for mail in mails:
    print("\t{}".format(mail))

print("-"*50)

import re

no = 1234567898
if(len(no.strip())==10):
    res = re.search("/d{10}",no)
    if res != None:
        print("Valid")
    else:
        print("Not")
else:
    print("10")


import mysql.connector

con = mysql.connector.connect(host = "localhost", user="root",passwd = "root")
cur = con.cursor()
print("connect")


#lambda  fun

res = lambda a,b:a+b
print(res(32,32))

lt1 =["ram"]
print(lt1[0][2])


try:
    print(10/5)
except(ZeroDivisionError):
    print("sorry")
finally:
    print("comtinues")

'''
with open("hello.py","a") as fd:
    fd.read()
        







    
