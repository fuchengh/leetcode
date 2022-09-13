class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key: value of number, value: index
        
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in seen.keys():
                return [seen[remain], idx]
            else:
                # add current to table
                seen[num] = idx
        