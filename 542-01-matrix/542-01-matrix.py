class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[0] * len(mat[0])] * len(mat)
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    right = mat[r][c+1] if c < n-1 else math.inf
                    bottom = mat[r+1][c] if r < m-1 else math.inf
                    mat[r][c] = min(mat[r][c], right+1, bottom+1)
        
        return mat