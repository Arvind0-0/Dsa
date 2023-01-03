    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(A[0])):
            tmp = [ele[i] for ele in A]
            tmp_sort = sorted(tmp)
            if tmp !=tmp_sort:
                res+=1
                
        return res
