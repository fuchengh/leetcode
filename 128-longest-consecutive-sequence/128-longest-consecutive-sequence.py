class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                curr_streak = 1
                
                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1
            
                longest = max(longest, curr_streak)
        
        return longest