#re_ex_3

import re

str1 = "abbcdeaaffgaaaqrsv "

spat = re.finditer("z",str1)

for i in spat:
    print("start= {}, end= {}, gr= {}".format(i.start(),i.end(),i.group()))
    print()
