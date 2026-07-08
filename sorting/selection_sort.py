# selection sort for assending order
# key points 
# i inital arr[o]
# min_index = i
# j= i+1
# find and swap 
def selection_assending(nums):
  n = len(nums)
  for i in range(n-1):
    min_ind = i
    for j in range(i+1, n):
      if nums[j] < nums[min_ind]: 
        min_ind  =  j
      
    nums[i], nums[min_ind] = nums[min_ind], nums[i]
     
  return nums

nums = [10,2,3,4,1,7,8]

print(selection_assending(nums))

# selection sort for dessending order

def selection_dessending(nums):
  n = len(nums)
  for i in range(n-1):
    max_ele = i
    for j in range(i+1, n):
      if nums[max_ele] < nums[j]:
        max_ele = j;
    nums[i] , nums[max_ele] = nums[max_ele], nums[i]
  return nums

print(selection_dessending(nums))


