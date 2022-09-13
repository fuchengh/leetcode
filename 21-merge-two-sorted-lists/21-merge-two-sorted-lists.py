# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=None)
        orig = dummy
        
        ptr1 = l1
        ptr2 = l2
        
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    dummy.next = ptr1
                    ptr1 = ptr1.next
                else:
                    dummy.next = ptr2
                    ptr2 = ptr2.next
            elif ptr1 and not ptr2:
                dummy.next = ptr1
                ptr1 = ptr1.next
            else:
                dummy.next = ptr2
                ptr2 = ptr2.next
            dummy = dummy.next
        
        return orig.next