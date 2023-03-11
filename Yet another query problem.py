class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        suffixocc = [0] * N
        suffixmap = dict()
        for i in range(N - 1, -1, -1):
            if A[i] not in suffixmap:
                suffixmap[A[i]] = 1
            else:
                suffixmap[A[i]] += 1
            suffixocc[i] = suffixmap[A[i]]
        
        arr = [suffixocc[l:r + 1].count(k) for l, r, k in Q]
        return arr
