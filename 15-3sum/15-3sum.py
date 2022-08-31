class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(curr, target, left, right):
            res = []
            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ == target:
                    res.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                elif sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
            return res

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort()
        res = set()
        for i in range(len(nums) - 3):
            if nums[i] > 0:
                break
            remain = 0 - nums[i]
            left = i + 1
            right = len(nums)-1
            for r in twoSum(i, remain, left, right):
                res.add(tuple(r))
            
        return list(res)