
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr)//2
  left_arr=arr[:mid]
  right_arr=arr[mid:]
  left = merge_sort(left_arr)
  right=merge_sort(right_arr)
  return merge_array(left,right)
    

def merge_array(left, right):
  i = j =0
  n = len(left)
  m = len(right)
  result = []
  while i<n and j<m:
    if(left[i] <= right[j]):
     result.append(left[i])
     i += 1
    else:
      result.append(right[j])
  if(i<n):
    result.append(left[i])
    i +=1
  if(j<m):
    result.append(right[j])
    j +=1
  return result
 


arr = [3,1,2,4,1,5,2,6,4]
print("hellow soring")

print(merge_sort(arr))