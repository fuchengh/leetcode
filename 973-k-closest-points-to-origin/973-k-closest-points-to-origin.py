class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            dist.append((d, p))
        
        dist.sort(key = lambda x: x[0])
        
        return [x[1] for x in dist[:k]]