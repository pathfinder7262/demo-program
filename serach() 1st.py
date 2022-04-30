#serach() 1st

import re

g_str = "python is oops lang and python is pop lang"

spat = "python"

fdata = re.finditer(spat,g_str)

for i in fdata:
    print(i)
