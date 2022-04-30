#filter obj ex_1

def posi(x):
    if x >0:
        return True
    else:
        return False

def neg(x):
    if x <0:
        return True
    else:
        return False
        
lst1 = [1,2,3,-3,-5,8,-9,-4,7]

pos_obj = list(filter(posi,lst1))
print("Positive int: ",pos_obj)


neg_obj = tuple(filter(neg,lst1))
print("Negative int: ",neg_obj)
