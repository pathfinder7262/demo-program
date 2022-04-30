#armstrong number:

def arm(n):
    sum1 = 0
    temp = n
    while temp>0:
        digit = temp %10
        sum1 = sum1+digit**3
        temp//=10
        return sum1
        
    if sum1 == n:
            print("Number is armstrong: ")
    else:
           print("Not")
           
print(arm(153))
