# fact of 4 is = 24
# 1*2*3*4 = 24

def fact(n):
  if n == 1:
    return 1
  return(n*fact(n-1))

result = fact(3)
print(result)