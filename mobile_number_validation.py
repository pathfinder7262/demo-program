#mobile_number_validation


import re

mob = input("Enter the mobile number:  ")

if(len(mob.strip())) == 10:
    if (re.search("\d{10}",mob)) != None:
        print("Valid ")
    else:
        print("Not Valid")
else:
    print("Please enter the 10 digit ")
