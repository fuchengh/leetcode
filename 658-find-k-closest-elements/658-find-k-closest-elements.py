class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for n in arr:
            dist = -abs(x-n)
            if len(heap) == k:
                top = heappop(heap)
                if top[0] < dist:
                    heappush(heap, (dist, n))
                else:
                    heappush(heap, top) # push back to heap again
            else:
                heappush(heap, (dist, n))
        
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])
        
        return sorted(res)