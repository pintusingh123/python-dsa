arr = [6,9,1,4,2]
count = 0
for i in arr:
  count +=1
print(count)

n = count
for i in range(0,n-1):
  min = i
  for j in range(i+1, n):
    if(arr[j] < arr[min]):
      min = j
  arr[i],arr[min] = arr[min], arr[i]

print(arr)