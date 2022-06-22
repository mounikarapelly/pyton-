from  array import *

vals= array('i',[2,3,4,5,6,7,8])
newArr = array(vals.typecode, (a*a for a in vals))


for e in newArr:

    print(e)