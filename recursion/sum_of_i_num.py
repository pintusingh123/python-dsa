# print the program for sum of 1 to n num parameterise fun recursion

# simple exmpl 1
def sumfun(sum,i , n):
  if i > n:
    print(sum)
    return
  sumfun(sum+i, i+1, n)

sumfun(0 , 1, 4)
print()

# best way  functional recursion -n, sc-n
def sumfun2(n):
  if n == 1:
    return 1
  return n+sumfun2(n-1)
result = sumfun2(4)
print(4)