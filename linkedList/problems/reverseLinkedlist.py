# write the code for print reverse order of a linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Sll:
  def __init__(self):
    self.head = None
  
  def append(self, value):
    newNode = Node(value)
    if self.head is None: # when linked list is empty then new node will be head of the linked list
      self.head = newNode
    else:
      currentEle = self.head
      while(currentEle.next != None):
        currentEle = currentEle.next
      currentEle.next = newNode
 
  def traversal(self):
   if (self.head is None):
    print("SLL is empty")
   else:
    currentEle = self.head
    while currentEle is not None:
       print(currentEle.data, end=" ")
       currentEle = currentEle.next
    print()

  def reversalList(self):
     pass

  def bruthForceReversal(self):
    # NOTE : this is not the optimal solution for reversing a linked list but it is a brute force solution for reversing a linked list
  #  tc : O(n) sc : O(n) we use extra space for stack to store the elements of the linked list
    temp = self.head 
    stack = []
    while temp is not None:
      stack.append(temp.data)
      temp = temp.next
    
  
    temp = self.head
    while temp is not None:
      stackele = stack.pop()
      temp.data = stackele
      temp = temp.next
    return self.head
  def optimalReversal(self):
    # NOTE : this is the optimal solution for reversing a linked list
    # tc : O(n) sc : O(1) we don't use extra space for stack to store the elements of the linked list
    prev = None
    current = self.head
    while current is not None:
      currentNextNode = current.next
      current.next = prev
      prev = current
      current = currentNextNode
    self.head = prev
    

sll = Sll()
sll.append(1)
sll.append(2)
sll.append(3)
sll.traversal()
# result = sll.bruthForceReversal()
sll.optimalReversal()
print("after reversal")
sll.traversal()