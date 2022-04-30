#re_ex_2
import re
noc = 0
src_ptn = "[a-z]"
cc_mtch = re.finditer(src_ptn,"AaHtFcObgiR#^c7%4$%c6hc$7%(kGvCKI8&")
for i in cc_mtch:
    print("Find the all charcter z:"
                "Starting index: {} \t"
                "Ending index: {} \t"
                "Grop: {}".format(i.start(),i.end(),i.group()))
    noc = noc+1
print("Occurence of charcter  :",noc)
print("==="*30)
