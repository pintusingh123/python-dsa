

class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head
         

        # Phase 1: detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
           

            if slow == fast:
              count = 1
              temp = slow.next
              while temp != slow:
                  count += 1
                  temp = temp.next
              return count

        return None
    