class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0 # performed operations
        while target > startValue:
            count += 1
            if target % 2 == 1:
                # if target is odd, add target by 1
                target += 1
            else:
                # if target is even, divide it by 2
                target //= 2
        # remaining = startValue - target (for add operations)
        return count + startValue - target