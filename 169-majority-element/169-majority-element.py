class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        
        for n in nums[1:]:
            if n != major:
                count -= 1
                if count <= 0:
                    count = 1
                    major = n
            else:
                count += 1
        
        return major