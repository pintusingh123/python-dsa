# key points
# i init from n-1  
# j run 0 to i
# adjacent ele compare and swap 

def buble_assending(num):
  n = len(num)
  for i in range(n-1, 0,-1):
    for j in range(0,i):
      if num[j] > num[j+1]:
        num[j] ,num[j+1] = num[j+1],num[j]
  return num
num = [6,1,5,2,4,3]
print(buble_assending(num))

def buble_dessending(num):
  n = len(num)
  for i in range(n-1,0,-1):
    for j in range(0,i):
      if num[j]<num[j+1]:
        num[j] ,num[j+1] = num[j+1],num[j]
  return num
num2 = [6,1,5,2,4,3]
print(buble_dessending(num2))