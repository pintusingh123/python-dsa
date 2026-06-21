#ex nitin is a palindrome
num = 191
n = num
reverse = 0
while n > 0 :
  digit = n%10
  reverse = (reverse * 10) + digit
  n = n//10

if num == reverse:
  print("it is palindrome")
else:
  print("not palindrome")
# print(reverse)

# tc (log base) N 