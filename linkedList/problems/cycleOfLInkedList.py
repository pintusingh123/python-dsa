# solv this problem , cycle of linked list

# method 1 : using hash set to store the visited nodes of the linked list and check if the current node is already visited or not if it is already visited then there is a cycle in the linked list otherwise there is no cycle in the linked list
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Sll:
  def __init__(self):
    self.head = None

    # tc is O(n) and sc is O(n) because we are using hash set to store the visited nodes of the linked list
  def CycleOfLinkedListBruteForce(self):
    temp = self.head
    hashSet = set()
    while temp is not None:
      if temp in hashSet:
        return True
      hashSet.add(temp)
      temp = temp.next
    return False
  
  # method 2 : using two pointers to find the cycle of linked list
  # tc is O(n) and sc is O(1) because we are using two

  def CycleOfLinkedListOptimal(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
      return False