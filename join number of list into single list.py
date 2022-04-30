#join number of list into single list
from itertools import chain
lst = [list(range(0,10)) for _ in range(10)]
print(lst)


# list(chain(*lst))
r = []
for i in lst:
    r.extend(lst)
print(r)
    
