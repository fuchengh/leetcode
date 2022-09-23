# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode(-1, next=None)
        orig = sort
        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                sort.next = ListNode(p1.val, next=None)
                p1 = p1.next
            else:
                sort.next = ListNode(p2.val, next=None)
                p2 = p2.next
            sort = sort.next
        
        while p1:
            sort.next = ListNode(p1.val, next=None)
            sort = sort.next
            p1 = p1.next
        
        while p2:
            sort.next = ListNode(p2.val, next=None)
            sort = sort.next
            p2 = p2.next
        
        return orig.next