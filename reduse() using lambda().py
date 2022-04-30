#add all element in tpl using reduse() using lambda()

import functools

print("Total is: ",functools.reduce(lambda x,y: x+y,(2,3,5,8,9,1)))
