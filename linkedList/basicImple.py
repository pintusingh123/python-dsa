# linkedlist in python dynamiclly type
# each node contain data nad next node-reference
# last node ka next none initialize hota hai 
# python does't have  pointer its use references 
# example
# [ (data | next-node) -> (data | next-node) -> (data | node) ]
 
class Node:
  def __init__(self ,data):

    self.data = data
    self.next = None

class SLL:
  def __init__(self) -> None:
     self.head = None

  def append(self , data):
    newNode = Node(data)
    # if self.head is Node
    if (self.head is None):
      self.head = newNode
    else:
      current = self.head
      while(current.next != None):
          current = current.next
      current.next = newNode
  
  def traversal(self):
  
    if(self.head is None):
      print("sll is empty")
    else:
     current = self.head
     while (current != None):
        print(current.data , end=" ")
        current = current.next
     print()
  
  def insertAt(self , value , posi):
    newNode = Node(value)
    if(posi == 0):
      newNode.next = self.head
      self.head = newNode
    else:
      current = self.head
      preveNode = None
      count = 0
      while (current is not None and count < posi):
        preveNode = current
        current = current.next
        count += 1
      preveNode.next = newNode
      newNode.next = current

  def delete(self, val):
    temp = self.head
    if(temp.next is None):
      if temp.data == val:
       self.head = temp.next
       return
    else:
      fount = False
      prev = None
      while temp is not None:
        if temp.data == val:
           fount = True
           break
        prev = temp
        temp = temp.next
      if fount:
        prev.next = temp.next
        return
      else:
        print("Node Not Found")

sll = SLL()
sll.append(1)
sll.append(12)
sll.append(13)
sll.append(14)
sll.traversal()