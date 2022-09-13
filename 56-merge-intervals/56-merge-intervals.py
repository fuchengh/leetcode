class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
        intv.sort()
        q = deque(intv[1:])
        ans = [intv[0]]
        
        while q:
            cur = q.popleft()
            start, end = cur
            
            if start <= ans[-1][1]:
                # overlapped, merge
                ans[-1][1] = max(end, ans[-1][1])
            else:
                # not overlapped, add to ans
                ans.append([start, end])
        
        return ans