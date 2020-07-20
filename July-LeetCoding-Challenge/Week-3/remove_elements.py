'''
# Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example:

    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5


'''
# SOLUTION:
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 1.
        # ITERATIVE
        dummy = ListNode(-1)
        dummy.next = head
        
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
        
        # 2.
        # RECURSIVE
        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
