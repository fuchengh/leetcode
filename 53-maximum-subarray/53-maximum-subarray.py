class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -math.inf
        cur = 0
        
        for n in nums:
            cur += n
            if cur > ans:
                ans = cur
            if cur < 0:
                cur = 0
        
        return ans