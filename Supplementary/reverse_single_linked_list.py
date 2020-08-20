# Reverse a Singly Linked List

# SOLUTION:
# Definition of a SinglyLinkedList
# def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            prv = curr.next
            curr.next = prev
            prev = curr
            curr = prv
        head = prev
        return head
        
        # A more easy and pythonic way 
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
   
