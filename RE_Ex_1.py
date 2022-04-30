#RE_Ex_1
import re

cc_mtch = re.finditer("[abc]","AaHtFcObgiR#^c7%4$%c6hc$7%(kGvCKI8&")

noc = 0
for i in cc_mtch:
    print("Find the specific character:"
                "Starting index: {} \t"
                "Ending index: {} \t"
                "Grop: {}".format(i.start(),i.end(),i.group()))
    noc = noc+1
print("Occurence of abc:",noc)
print("==="*30)

noc = 0
cc_mtch = re.finditer("[^abc]","AaHtFcObgiR#^c7%4$%c6hc$7%(kGvCKI8&")
for i in cc_mtch:
    print("Find the all charcter except abc:"
                "Starting index: {} \t"
                "Ending index: {} \t"
                "Grop: {}".format(i.start(),i.end(),i.group()))
    noc = noc+1
print("Occurence of charcter except abc:",noc)
print("==="*30)

noc = 0
cc_mtch = re.finditer("[^abc]","AaHtFcObgiR#^c7%4$%c6hc$7%(kGvCKI8&")
for i in cc_mtch:
    print("Find the all charcter except abc:"
                "Starting index: {} \t"
                "Ending index: {} \t"
                "Grop: {}".format(i.start(),i.end(),i.group()))
    noc = noc+1
print("Occurence of charcter except abc:",noc)
print("==="*30)

noc = 0
cc_mtch = re.finditer("[A-Z]","AaHtFcObgiR#^c7%4$%c6hc$7%(kGvCKI8&")
for i in cc_mtch:
    print("Find the all charcter except abc:"
                "Starting index: {} \t"
                "Ending index: {} \t"
                "Grop: {}".format(i.start(),i.end(),i.group()))
    noc = noc+1
print("Occurence of charcter A-Z:",noc)
print("==="*30)
