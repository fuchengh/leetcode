# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(val=-1, next=head)
        s = f = prev
        orig_head = prev
        
        for i in range(n):
            if f:
                f = f.next
                
        while s and f:
            prev = s
            s = s.next
            f = f.next
        
        prev.next = prev.next.next # del s
        
        return orig_head.next