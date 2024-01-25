# Author: Alex Gezerlis
# Numerical Methods in Physics with Python (CUP, 2020)

def look(target,names):
    for name in names:
        if name==target:
            val = name
            break
    else:
        val = None
    return val

names = ["Ezekiel", "Bill", "John"]
print(look("Eve", names))
print(look("Jack", names))
