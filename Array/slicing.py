from array import *
val = array("i", [12,3,4,5,6,7,8,9]);

for i in range(0, len(val)) : 
   print(val[i] , end=" ")

print("\n")

#  slicing 
s = val[::-1] #revers order 

for i in range(0 , len(s)) :
   print(s[i], end=" ")