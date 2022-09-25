# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        s = head
        f = head.next
        
        while s != f:
            if f is None or f.next is None:
                return False
            s = s.next
            f = f.next.next
        
        return True
        