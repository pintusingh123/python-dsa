class Stack:
  def __init__(self):
    self.stack =[];
  
  def insert(self,item):
    self.stack.append(item);
  
  def length(self):
    return len(self.stack);

  def remove(self):
    if self.length() == 0:
      return "Stack is empty";
    return self.stack.pop();
  
  def peek(self):
    if self.length() == 0:
      return "Stack is empty";
    return self.stack[-1];
  