class Solution:
    def concatenatedBinary(self, n: int) -> int:
        c = ""
        
        for i in range(1, n+1):
            b = bin(i)
            c += str(b)[2:]
        
        return int(c, 2) % (10**9+7)