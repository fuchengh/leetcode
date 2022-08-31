class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            # find left char
            while not s[left].isalnum():
                if left == right:
                    break
                left += 1
            # find right char
            while not s[right].isalnum():
                if left == right:
                    break
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True