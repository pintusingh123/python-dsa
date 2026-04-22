from array import *
 
arr = array('i', [1,2,3,4,5,6])

for i in range(0, len(arr)) :
  print(arr[i], end=" ")

print("\n")

# inserting 
# arr.insert(2, 54); #specific position
# arr.append(887) #last 
# arr[3] = 100; # override 4 to 100 

for i in range(0, len(arr)) :
   print(arr[i], end=" ")
   

print("\n")

# Copy one arr to another array way1
copyarr = array(arr.typecode, (x*2 for x in arr))

for i in range(0, len(copyarr)) :
  print(copyarr[i], end=" ")

# deletion --------------------

print("\n")
# copyarr.pop(1)index base or last mai se delete hoga

copyarr.remove(8) #ele value direct delete hoti hai jese ki 8 ele hai index nahi hai

# copyarr.clear() # empty array
for i in range(0, len(copyarr)) :
  print(copyarr[i], end=" ")

# deletion