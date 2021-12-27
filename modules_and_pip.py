# print("Hello world")
# modules is how we import stuff.
# We are going to import from a file called
# "useful_tools.py"


import useful_tools
# This is similar to #include "file.h"


from useful_tools import fet_in_mile as ftcon

print(useful_tools.roll_dice(10))

# Roll ten-sided die

# ftcon.str()
# str(ftcon)

print("Feet in miles: " + str(ftcon))
