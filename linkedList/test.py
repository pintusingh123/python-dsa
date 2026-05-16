class Node:
  def __init__(self , data):
    self.data = data
    self.next = None

class Sll:
  def __init__(self):
    self.head = None
  
  def append(self, value):
    newNode = Node(value)
    if (self.head is None):
      self.head = newNode
    else:
      currentele = self.head
      while( currentele.next is not None):
        currentele = currentele.next
      currentele.next = newNode
  def traversal(self):
    if self.head is None:
      print("sll is empty")
    else:
      currentele = self.head
      while(currentele is not None):
        print(currentele.data)
        currentele = currentele.next

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


sll = Sll()
sll.append(1)
sll.append(12)
sll.append(13)
sll.traversal()
sll.delete(12)
sll.traversal()  