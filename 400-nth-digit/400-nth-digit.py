class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        
        # find level of n
        digits = 2
        nums = 90
        total = 9 + digits*nums
        
        while total < n:
            digits += 1
            nums *= 10
            total += digits * nums
        
        total -= digits * nums
        nums //= 10
        
        num, remain = divmod(n-total, digits)
        start = 10**(digits-1)-1
        
        if remain == 0:
            return int(str(start+num)[-1])
        else:
            return int(str(start+num+1)[remain-1])