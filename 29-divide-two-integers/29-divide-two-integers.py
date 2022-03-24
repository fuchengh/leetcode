class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2 ** 31
        # special case
        if dividend == MIN_INT and divisor == -1: return MAX_INT
        
        # Convert both numbers to negatives, and count neg signs
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        quotient = 0
        power = 1
        powers = []
        doubles = []
        
        while divisor >= dividend:
            powers.append(power)
            doubles.append(divisor)
            power += power
            divisor += divisor
        
        for i in range(len(doubles)-1, -1, -1):
            if doubles[i] >= dividend:
                quotient += powers[i]
                dividend -= doubles[i]
        # if either divisor or dividend is negative, return -quotient
        return quotient if negatives != 1 else -quotient