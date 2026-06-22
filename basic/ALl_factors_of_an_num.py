# write a program for solv how to find all factors of an numb
#  like 10 all factors is  1,2,5

# easy way approch
from math import sqrt
num1 = 10
for i in range(1, num1+1):
  if num1 % i == 0:
    print(i)

print("next")

# opptimize approch
num  = 36 
result = []
for i in range(1, int(sqrt(num))):
  if num % i ==0:
    result.append(i)
    if i != num //i:
      result.append(num//i)

print(result)