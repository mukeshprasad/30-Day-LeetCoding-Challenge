'''
# Reorder List

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
  reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:
  Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:
  Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# SOLUTION: O(N) Time

# Definition of a SinglyLinkedList
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # head pointer of 2nd half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow         # slow  being the head of 2nd half
        prev = None
        
        # Reverse the second half
        while curr:
            prv = curr.next
            curr.next = prev
            prev = curr
            curr = prv
            
        first = head
        second = prev
        # Merging appropriately
        while second and second.next:
            t1 = first.next
            first.next = second
            t2 = second.next
            second.next = t1
            first = t1
            second = t2
