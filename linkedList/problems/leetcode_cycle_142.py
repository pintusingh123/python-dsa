# this is a solution to the problem of detecting a cycle in a linked list and finding the starting node of the cycle. The algorithm uses the Floyd's Tortoise and Hare approach, which involves two pointers (slow and fast) to traverse the linked list.
class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        # Phase 1: detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Phase 2: find cycle start
                pointer1 = head
                pointer2 = fast
                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                return pointer1

        return None
    