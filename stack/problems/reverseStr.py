from collections import deque
stack = deque()
def reverse_string(string):
  #  store char of str in stacl
  for ch in string:
    stack.append(ch);

  # pop char from stack and add to result
  result = "";
  while len(stack) > 0:
   result = result + stack.pop();
  return result;

print(reverse_string("hellow bhai"))