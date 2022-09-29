class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [None] * n
        suffix = [None] * n
        prefix[0] = 1
        suffix[-1] = 1
        
        # build prefix array
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        # build suffix array
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        
        return res