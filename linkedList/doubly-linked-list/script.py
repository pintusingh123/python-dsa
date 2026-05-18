# creating Dll
class Node:
  def __init__(self,data):
     self.data = data
     self.next = None
     self.prev = None

class Dll:
   def __init__(self):
    self.head = None
   def insert_at_head(self,data):
     new_node = Node(data)
     if self.head is None:
       self.head = new_node
     else:
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node
 

   def insert_at_tail(self,data):
     new_node = Node(data)
     if self.head is None:
      self.head = new_node
     else:
       currentEle = self.head
       while currentEle.next is not None:
         currentEle = currentEle.next
       currentEle.next = new_node
       new_node.prev = currentEle

   def insert_at_position(self,data,pos):
      newNode = Node(data)
      if pos == 0:
       self.insert_at_head(data)
      else:
        currentEle = self.head
        count = 0
        while currentEle and count <pos-1:
          currentEle = currentEle.next
          count += 1
        if currentEle is None:
          print("position out of bound")
        
        newNode.next = currentEle.next
        newNode.prev = currentEle
        if currentEle.next is not None:
          currentEle.next.prev = newNode
        currentEle.next = newNode
   def delete_at_position(self,pos):
     pass
   def delete_at_head(self):
     pass
   def delete_at_tail(self):
     pass    
   def print_lis(self):
     currentEle = self.head
     while currentEle is not None:
       print(currentEle.data,end=" ")
       currentEle = currentEle.next

dll = Dll()
dll.insert_at_head(1)
dll.insert_at_head(2)
dll.insert_at_head(3)
dll.insert_at_tail(4)
dll.insert_at_tail(40)
dll.insert_at_position(5, 2)
dll.print_lis()