#triple all element in lst using map

lst = [2,3,4,5,6,7,8]
print(list(map(lambda x: x*3,lst)))

#add 3 in given list using map
lst = [2,3,4,5,6,7,8]
print(list(map(lambda x: x+3,lst)))

#conver in uppercaseand lowercase and remove duplicate using map:

lst = ["o","p","D","q","a","R","t","w","I","R","a","D"]

print("UpperCase: ",list(map(lambda x: x.upper(),lst)))

print("LowerCase: ",list(map(lambda x:x.lower(),lst)))

print("Remove Duplicate: ",set(map(lambda x: x,lst)))

#Add 2 given list and print differnce bet list using map

lst1 = [6,5,3,9]
lst2=[0,1,7,7]

print("addition of lists: ",list(map(lambda x,y:(x+y,x-y), lst1,lst2)))

print("diff of lists: ",list(map(lambda x,y:x - y, lst1,lst2)))


#convert list int and tuple int into str list:
tpl = (9,8,7,5,3,3,1)
lst = [2,3,4,5,6,7,8]

print("str list: ",list(map(lambda x: str(x),tpl )))
print("str list 2: ",list(map(lambda x: str(x),lst )))


