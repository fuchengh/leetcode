class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxlen = 0
        q = deque([])
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        mins = 0
        while q:
            len_q = len(q)
            mins += 1
            for _ in range(len_q):
                r, c = q.popleft()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
        
        return max(mins-1, 0) if fresh == 0 else -1