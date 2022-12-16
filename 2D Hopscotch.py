class Solution:
    def hopscotch(self, n, m, mat, ty, i, j):
        i, j = 2*i + j%2, 2*j 
        res = 0
        
        if ty == 0:
            for di, dj in [[-2,0], [2,0], [-1,-2], [-1,2], [1,-2], [1,2]]:
                ni, nj = (i + di)//2, (j + dj)//2
                if 0 <= ni < n and 0 <= nj < m:
                    res += mat[ni][nj]
        else:
            for di, dj in [[-4,0], [4,0], [0,-4], [0,4], [-3,-2], [-3,2], [3,-2], [3,2], [-2,-4], [-2,4], [2,-4], [2,4]]:
                ni, nj = (i + di)//2, (j + dj)//2
                if 0 <= ni < n and 0 <= nj < m:
                    res += mat[ni][nj]
            
        return res
