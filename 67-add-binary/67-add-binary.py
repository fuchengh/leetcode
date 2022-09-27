class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            # set a to be the longer string
            a, b = b, a
        
        carry = 0
        res = ""
        ptra = len(a) - 1
        ptrb = len(b) - 1
        
        while ptrb >= 0:
            sum_ = carry + int(a[ptra]) + int(b[ptrb])
            if sum_ > 1:
                carry = 1
                sum_ %= 2
            else:
                carry = 0
            res += str(sum_)
            
            ptrb -= 1
            ptra -= 1
        
        while ptra >= 0:
            # add remaining values to res
            sum_ = int(a[ptra]) + carry
            if sum_ > 1:
                carry = 1
                sum_ %= 2
            else:
                carry = 0
            res += str(sum_)
            ptra -= 1
        
        # add carry if > 0
        if carry:
            res += "1"
        
        return res[::-1]