class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dups = set()
        res = set()
        seen = {}
        
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    comp = -val1 - val2
                    if comp in seen and seen[comp] == i: # answer found!
                        res.add(tuple(sorted((val1, val2, comp))))
                    seen[val2] = i
        
        return res