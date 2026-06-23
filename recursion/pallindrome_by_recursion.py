# def reverseStr(chars, start, end):
#     if start >= end:
#         return chars

#     chars[start], chars[end] = chars[end], chars[start]

#     return reverseStr(chars, start + 1, end - 1)


# s = "madam"

# chars = list(s)

# reversed_chars = reverseStr(chars, 0, len(s) - 1)

# reversed_str = "".join(reversed_chars)

# print(reversed_str)

# if s == reversed_str:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# pallindrome

def pall(s,left,right):
  if left >= right:
    return True
  if s[left] != s[right]:
   return False
  return pall(s,left+1,right-1)

s = "maduam"
ans = pall(s,0,len(s)-1)
print(ans)