#even odd using filter and lambda

even = lambda x: x % 2 == 0

odd = lambda x : x % 2 != 0

lst = [1,2,3,4,5,6,7,8,9,88,77,66,55,44,33,2,11]

ev_val = list(filter(even,lst))
print(ev_val)

od_val = set(filter(even,lst))
print(od_val)

