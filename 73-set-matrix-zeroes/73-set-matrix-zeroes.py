class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_zero_r = set([])
        set_zero_c = set([])
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    set_zero_r.add(r)
                    set_zero_c.add(c)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r in set_zero_r or c in set_zero_c:
                    mat[r][c] = 0