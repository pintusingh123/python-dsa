# write a program to find odd or even position of a linked list and return the odd position nodes first and then even position nodes in the linked list
# ---------------- NODE CLASS ----------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


#  LINKED LIST CLASS ----------------

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Print list
    def print_list(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


#  SOLUTION CLASS ----------------

class Solution:

    def oddEvenList(self, head):

        # Empty list or single node
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:

            # Connect odd nodes
            odd.next = even.next
            odd = odd.next

            # Connect even nodes
            even.next = odd.next
            even = even.next

        # Join odd list with even list
        odd.next = even_head

        return head


# ---------------- DRIVER CODE ----------------

sll = SinglyLinkedList()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

print("Original List:")
sll.print_list()

obj = Solution()

sll.head = obj.oddEvenList(sll.head)

print("\nAfter Odd-Even Rearrangement:")
sll.print_list()