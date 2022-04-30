array = []
size_of_array = int(input("Enter the size of array"))

for i in range(0,size_of_array):
    val = int(input("Enter the Number: "))
    array.append(val)

def avarg(array):
    lst2 = []
    lst2 = array[1::2]
    avrg = 0
    for i in lst2:
        avrg = (avrg+i)
    print(avrg//len(lst2))
        
avarg(array)

