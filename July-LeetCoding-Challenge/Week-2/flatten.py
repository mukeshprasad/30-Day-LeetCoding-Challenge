'''
# Flatten a Multilevel Doubly Linked List

# You are given a doubly linked list which in addition to the next and previous pointers,
  it could have a child pointer, which may or may not point to a separate doubly linked list.
  These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

# Example 1:

  Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
  Output: [1,2,3,7,8,11,12,9,10,4,5,6]
  
# Example 2:

  Input: head = [1,2,null,3]
  Output: [1,3,2]  

'''
# SOLUTION:
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 1. O(1) Space
        root = head
        while root:
            if not root.child:
                root = root.next
                continue
            tmp = root.child
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = root.next
            if root.next != None:
                root.next.prev = tmp
            root.next = root.child
            root.child.prev = root
            root.child = None
       return head
       
       # 2. O(h) Space - h -> no of levels
       stack = [head]
       p = Node(0)
       while stack:
          root = stack.pop()
          root.prev = p
          p.next = root
          p = root
          
          if root.next:
              stack.append(root.next)
          if root.child:
              stack.append(root.child)
              root.child = None
       head.prev = None
       return head
       
* Basic idea is straight forward:

1. Start form the head , move one step each time to the next node
2. When meet with a node with child, say node p,
  follow its child chain to the end and connect the tail node with p.next, by doing this we merged the child chain back to the main thread
3. Return to p and proceed until find next node with child.
4 .Repeat until reach null
