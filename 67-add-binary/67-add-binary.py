class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ptra = len(a) - 1
        ptrb = len(b) - 1
        
        ans = []
        carry = 0
        
        while ptra >= 0 and ptrb >= 0:
            sum_ = int(a[ptra]) + int(b[ptrb]) + carry
            ans.append(str(sum_ % 2))
            if sum_ > 1:
                carry = 1
            else:
                carry = 0
            
            ptra -= 1
            ptrb -= 1
        
        while ptra >= 0:
            sum_ = int(a[ptra]) + carry
            ans.append(str(sum_ % 2))
            if sum_ > 1:
                carry = 1
            else:
                carry = 0
            ptra -= 1
        while ptrb >= 0:
            sum_ = int(b[ptrb]) + carry
            ans.append(str(sum_ % 2))
            if sum_ > 1:
                carry = 1
            else:
                carry = 0
            ptrb -= 1
        if carry:
            ans.append("1")
        
        return "".join(ans[::-1])
        