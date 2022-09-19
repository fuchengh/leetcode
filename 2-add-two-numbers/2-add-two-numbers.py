# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        orig = l1
        
        p1 = l1
        p2 = l2
        prev_p1 = p1
        carry = 0
        
        while p1 and p2:
            sum = p1.val + p2.val + carry
            p1.val = sum % 10
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            prev_p1 = p1
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            sum = p1.val + carry
            p1.val = sum % 10
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            prev_p1 = p1
            p1 = p1.next
        
        while p2:
            sum = p2.val + carry
            prev_p1.next = ListNode(val=sum % 10, next=None)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            prev_p1 = prev_p1.next
            p2 = p2.next
        
        if carry:
            prev_p1.next = ListNode(val=1, next=None)
        
        return orig