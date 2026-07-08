arr=[6,9,1,4,2]
# key points
# i init from n-1  
# j run 0 to i
# adjacent ele compare and swap 

n = 0
for i in arr:
  n+=1
print(n)
for i in range(n-1,0, -1):
  for j in range(0 , i):
    if(arr[j] > arr[j+1]):
      arr[j],arr[j+1] = arr[j+1], arr[j]
print(arr)