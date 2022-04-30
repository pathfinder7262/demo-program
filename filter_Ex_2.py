#filter_Ex_2

sdef even(x):
    if x%2 == 0:
        return True
    else:
        return False

def odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

tpl1 = (1,2,3,4,5,6,7,8,9,12,34,65,78,98,54)

evn_ele = list(filter(even,tpl1))
print("Even : ",evn_ele)

odd_ele = list(filter(odd,tpl1))
print("Odd: ",odd_ele)
