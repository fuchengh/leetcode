class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        q = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        while q:
            cur = q.popleft()
            r, c = cur
            for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= x < rows and 0 <= y < cols and dist[x][y] == math.inf:
                    dist[x][y] = min(dist[x][y], dist[r][c] + 1)
                    q.append((x, y))
        
        return dist