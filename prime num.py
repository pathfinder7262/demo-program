def prime(n):
    if n>1:
        for i in range(2,n//2):
            if(n%i)==0:
                print("Not Prime")
                break
        else:
            print("Prime: ")
    else:
        print("Not Prime")

prime(23)
            
    
