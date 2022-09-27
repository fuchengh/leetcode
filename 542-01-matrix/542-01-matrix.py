class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[math.inf for j in range(len(mat[0]))] for i in range(len(mat))]
        
        # top-left
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i-1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j-1] + 1)
        
        # bottom-right
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if i < len(mat)-1:
                    res[i][j] = min(res[i][j], res[i+1][j] + 1)
                if j < len(mat[0])-1:
                    res[i][j] = min(res[i][j], res[i][j+1] + 1)
        
        return res