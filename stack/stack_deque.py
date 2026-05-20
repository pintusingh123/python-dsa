from collections import deque

stack = deque()

def insert(item):
  stack.append(item)
  
def length():
  return len(stack)

def remove():
  if length() == 0:
    return "Stack is empty"
  return stack.pop()

def peek():
  if length() == 0:
    return "Stack is empty"
  return stack[-1]

def is_empty():
  return length() == 0

insert(1)
insert(2)
insert(3)
print(peek())
