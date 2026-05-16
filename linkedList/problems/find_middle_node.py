# given linked list we need to find middle of the linked list and return it middle node of linked list

class Node:
  def __init__(self , data):
    self.data = data
    self.next = None

class SinglyList:
    def __init__(self):
     self.head = None

    def append(self , val):
      newNode = Node(val)

      if( self.head is None):
        self.head = newNode
      else:
        currentEle = self.head
        while(currentEle.next != None):
          currentEle = currentEle.next

        currentEle.next = newNode  
            
    def traversal(self):

      if(self.head == None):
        print("SLL is empty")
      else:
        currentEle = self.head
        while(currentEle != None):
           print(currentEle.data , end=" ")
           currentEle= currentEle.next 
      print()
    def middleOFList(self):
      slow = self.head
      fast = self.head
      while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
      print(slow.data , end=" ")


single = SinglyList()
single.append(1)
single.append(2)
single.append(3)
single.append(4)
single.append(5)
single.append(6)
single.traversal()
single.middleOFList()
 