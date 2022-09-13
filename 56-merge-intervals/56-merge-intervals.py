class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
        intv.sort()
        ans = [intv[0]]
        
        for i in range(1, len(intv)):
            start, end = intv[i]
            
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1]) 
            else:
                ans.append(intv[i])
            
        return ans