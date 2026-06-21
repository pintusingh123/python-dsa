num = 1234
n=num
ans = 0
while n > 0:
  lastdigit = n%10;
  ans +=lastdigit
  n = n//10

print(ans)
