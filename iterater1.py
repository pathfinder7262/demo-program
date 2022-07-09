'''
def fib(n):
    a = 0
    b = 1

    if n == 0:
        print(a)
    else:
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
            print( c)

fib(10)

#palindrom
def pal(str1):
    str2 = str1[::-1]
    if str1 == str2:
        print("true")
    else:
        print("false")

n = input("Enter the number or string: ")

pal(n)

#reverse a number
n =123224
a = 1
rev = 0
while(n>0):
    rev = (rev*10)+(n%10)
    n = n//10

print(rev)
'''


#reverse a str

a = "asdfg"
b = ""

for i in (1,len(a)+1):
    b +=  a[-i]

print(b)























    
    
