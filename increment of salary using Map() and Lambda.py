#increment of salary using Map() and Lambda

inc = lambda x : x +x*0.5  #10 + 10*0.5 => 10+5.0 => 15.0

tpl = (10,12,14,15,6,12)

inc_sal = list(map(inc,tpl))
print(inc_sal)

print("===========END=============")

#square of element using Map() and Lambda

print( list(map(lambda x : x*x ,(10,12,14,15,6,12)))  )




