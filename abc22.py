from matplotlib import lines

'''
f = open("abc33.txt",'r')
line = f.readlines()
print(line) 
f.close()
for i in line:
    line1 = i.split()
    reversed1 = " ".join(line1[::-1])
    print(reversed1)
'''
f = open("abc33.txt",'r')
line = f.readlines()
print(line) 
f.close()
ab = set(line)
res11 = ab.union()
print(res11)
