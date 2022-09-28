class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def twoSum(cur, target, start):
            seen = set()
            n = start
            while n < len(nums):
                comp = target-nums[n]
                if comp in seen:
                    res.append([cur, nums[n], comp])
                    while n+1 < len(nums) and nums[n] == nums[n+1]:
                        n += 1
                else:
                    seen.add(nums[n])
                # skip processed nums
                n += 1
                
                
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if (i > 0 and nums[i] != nums[i-1]) or i == 0:
                twoSum(nums[i], -nums[i], i+1)
        
        return res