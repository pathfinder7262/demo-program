#factorial number;

def fact(n):
    f = 1
    if n <0:
        print("Fact does not exist: ")
    elif n == 0:
        print("Fact is 0")
    else:
        
        for i in range(1,n+1):
            f = i * f

    print(f)

fact(7)

