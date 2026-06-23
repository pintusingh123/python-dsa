s = "nitin"
left =0
right = len(s)-1
def pall(s,left,right):
 while left <= right:  
  if s[left] != s[right]:
    return False
  left +=1;
  right -=1
 return True

ans  = pall(s,left,right)
print(ans)