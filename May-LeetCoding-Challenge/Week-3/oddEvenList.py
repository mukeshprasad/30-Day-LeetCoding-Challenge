'''
# Odd Even Linked List

# Given a singly linked list, group all odd nodes together followed by the even nodes.
  Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:
  Input: 1->2->3->4->5->NULL
  Output: 1->3->5->2->4->NULL

# Example 2:
  Input: 2->1->3->5->6->4->7->NULL
  Output: 2->3->6->7->1->5->4->NULL

# Note:
  The relative order inside both the even and odd groups should remain as it was in the input.
  The first node is considered odd, the second node even and so on ...

'''

# SOLUTION - 1: O(N) Time and O(1) Space

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is not None:
            odd = head
            even = head.next
            even_head = even
            while even is not None and even.next is not None:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = even_head
        return head
        
# SOLUTION -2 : Similar to previous

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 340149889 submission
        if head is None:
            return head
        odd_head= odd = ListNode()
        even_head = even = ListNode()
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = even_head.next
        return odd_head.next
