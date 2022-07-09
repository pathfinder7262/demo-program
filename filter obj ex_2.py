'''
def posval(x):
    if (x>0):
        return True
    else:
        return False

def negval( k ):
    if(k<0):
        return True
    else:
        return False

def sq(no):
    no = no*no
    return no

lst = [1,-2,3,-4,-5,6,-7]


res = map(sq,lst)
for i in res:
    print(i)

'''
import functools
lst = [2,5,1,7,4,0,9]
big=functools.reduce(lambda x,y: x if (x>y) else y, lst)
small=functools.reduce(lambda a,b: a if (a<b) else b, lst)
print("---------------------------------")
print("Biggest({})={}".format(lst,big))
print("Smallest({})={}".format(lst,small))

def sort1(x,y):
    c = ""
    if x<y:
        c = x
        x = y
        y = c

        return












