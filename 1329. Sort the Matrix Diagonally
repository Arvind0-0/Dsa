class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat)==0:
            return mat
        n, m = len(mat), len(mat[0])
        i,j = len(mat)-1, 0
        for i in range(0,len(mat)):
            t, k = i,0
            tmp = []
            while t<n and k<m:
                tmp.append(mat[t][k])
                t+=1
                k+=1
            tmp.sort()
            t, k, j = i,0, 0
            while t<n and k<m:
                mat[t][k] = tmp[j]
                t+=1
                k+=1
                j+=1
        for j in range(1, m):
            t, k = 0, j
            tmp = []
            while t<n and k<m:
                tmp.append(mat[t][k])
                t+=1
                k+=1
            tmp.sort()
            t, k, j = 0,j, 0
            while t<n and k<m:
                mat[t][k] = tmp[j]
                t+=1
                k+=1
                j+=1
        return mat
