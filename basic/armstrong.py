# 153 Ek number Armstrong tab hota hai jab uske har digit ki power (number of digits) ka sum original number ke equal ho.

# step 1 count lengh
# step 2 find last digit 
# step 3 mutliply lastdigit ** length

num  = 153
n = num
n2 = num
length = 0
armstrong  = 0
while n > 0:
  length +=1
  # Lastdigit = n%10
  n = n//10
print(length)

while n2 >0:
  digit = n2 % 10
  armstrong +=(digit ** length)
  n2 = n2//10
if armstrong == num:
  print("is armstrong")
else:
  print("not armstrong")

print(armstrong)

