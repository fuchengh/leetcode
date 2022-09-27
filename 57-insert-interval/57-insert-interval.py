class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ptr = 0
        res = []
        
        while ptr < len(intervals):
            if intervals[ptr][0] > newInterval[0]:
                break
            res.append(intervals[ptr])
            ptr += 1
        
        # push new interval to res
        if len(res) > 0 and res[-1][1] >= newInterval[0]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        
        # push the remaining intervals
        while ptr < len(intervals):
            cur = intervals[ptr]
            if len(res) > 0 and res[-1][1] >= cur[0]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
            ptr += 1
        
        return res