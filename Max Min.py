class Solution:
    def findSum(self,A,N): 
        A.sort()
        res = A[0]+A[N-1]
        return res
