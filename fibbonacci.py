#fibbonacci

def fibb(n):
    n1 ,n2 = 0,1
    count = 0
    if n <= 0:
        print("number is less than 0")
    elif n == 0:
        print("Number is zero")
    else:
        print("Fibbo: ")
        while count<n:
            print(n1)
            nth = n1 +n2
            #swap
            n1 = n2
            n2 = nth
            count = count+1
        
fibb(10)   
