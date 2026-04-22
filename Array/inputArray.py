from array import *
arr = array('i' , [])

n = int(input("enter A num for length of array ele"))

for i in range(0, n) :
  arr.append(int(input("enter Next input ele")))

for x in arr:
  print(x, end=" ")