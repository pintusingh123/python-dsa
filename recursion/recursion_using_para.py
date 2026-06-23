# case 1 
# def fun(x,n):
#   if n ==0:
#     return
#   print(x)
#   fun(x-1, n-1)
# result = fun(14,5)
 

#  print 1 to n using head reurion  increasing order
# def fun (x,n):
#    if x < n:
#       return
#    fun(x-1, n)
#    print(x)

# fun(4, 1)


# print n to 1 using head recursion decreasing order
# def fun(x,n):
#   if x > n:
#     return
#   fun(x+1,n)
#   print(x)
 
# fun(1,5)

# print 1 to n using tail increasing order
# def fun(x,n):
#   if x > n:
#     return

#   print(x)
#   fun(x+1,n)
# fun(1,5)

# print n to 1 using tail recursion decreasing order 
def fun (x,n):
  if x < n:
   return
  print(x)
  fun(x-1,n)
fun(4,1)