# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        
        while cur:
            if cur.next:
                orig_next = cur.next
            else:
                orig_next = None
            cur.next = prev
            prev = cur
            cur = orig_next
            
        return prev