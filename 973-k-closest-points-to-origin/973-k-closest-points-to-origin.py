class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            heappush(heap, (-dist, p[0], p[1])) # implement max-heap
            # so when we pop it, it will pop the max val in current heap
            if len(heap) == k + 1:
                heappop(heap)
            
        
        return [[x, y] for d, x, y in heap]
            