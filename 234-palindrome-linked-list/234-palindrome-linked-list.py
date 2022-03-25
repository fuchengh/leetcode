# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half
        prev = None
        while slow:
            original_next = slow.next
            slow.next = prev
            prev = slow
            slow = original_next
        
        first_start = head
        second_start = prev
        
        while second_start:
            if not second_start.next:
                break
            if first_start.val != second_start.val:
                return False
            
            first_start = first_start.next
            second_start = second_start.next
        return True