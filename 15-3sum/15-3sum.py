class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(x):
            seen = set()
            y = x + 1
            while y < len(nums):
                remain = 0 - nums[x] - nums[y]
                if remain in seen:
                    res.append([nums[x], nums[y], remain])
                    while y+1 < len(nums) and nums[y] == nums[y+1]:
                        y += 1
                
                seen.add(nums[y])
                y += 1
        
        nums.sort()
        res = []
        
        for x in range(len(nums)-2):
            if nums[x] > 0:
                break
            if x == 0 or nums[x] != nums[x-1]:
                twoSum(x)
        
        return res