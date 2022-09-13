class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_freq = 1
        cur_ans = nums[0]
        
        for n in nums[1:]:
            if n != cur_ans:
                cur_freq -= 1
                if cur_freq < 0:
                    cur_ans = n
                    cur_freq = 1
            else:
                cur_freq += 1
        
        return cur_ans