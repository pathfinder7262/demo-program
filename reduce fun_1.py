import functools
#prtogram for finding sum of all elements of list
#lst=[5,6,7,8,10,20,30,40]
tpl=(2,3,5,8,9,1)
result=functools.reduce(lambda x,y:x+y, tpl) # reduce() is present in "functools" module
print("sum={}".format(result))
