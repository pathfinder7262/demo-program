# prime number:

flag = False
def prime(n):
    if n>1 :
        for i in range(2, (n//2)):
           
            if (n % i) == 0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("Not prime number")
                

prime(21)


    
