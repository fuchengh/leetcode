class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.sort()
        idx = 0
        
        while idx < len(intervals):
            if intervals[idx][0] >  newInterval[0]:
                break
            ans.append(intervals[idx])
            idx += 1
        
        # insert new interval
        if ans and ans[-1][1] >= newInterval[0]:
            # overlaps
            ans[-1][1] = max(newInterval[1], ans[-1][1])
        else:
            ans.append(newInterval)
        
        # insert remaining intervals, might need to merge
        while idx < len(intervals):
            if intervals[idx][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[idx][1], ans[-1][1])
            else:
                ans.append(intervals[idx])
            idx += 1
        
        return ans