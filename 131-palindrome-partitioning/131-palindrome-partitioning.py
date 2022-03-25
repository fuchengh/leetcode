class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    # add to path if substring is a palindrome
                    path.append(s[start:i+1])
                    backtrack(i+1, path)
                    path.pop()
        res = []
        backtrack(0, [])
        return res