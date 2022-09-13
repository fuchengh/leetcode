class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        idx = 0
        
        # add intervals before newInterval
        while idx < len(intervals) and intervals[idx][0] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1
        
        # add new interval
        if ans and newInterval[0] <= ans[-1][1]:
            # new intervla overlaps with previous
            ans[-1][1] = max(ans[-1][1], newInterval[1])
        else:
            # not overlapping, just add to ans
            ans.append(newInterval)
        
        # add remaining intervals
        while idx < len(intervals):
            intv = intervals[idx]
            # might need to merge intervals
            if intv[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intv[1])
            else:
                ans.append(intv)
            
            idx += 1
        
        return ans