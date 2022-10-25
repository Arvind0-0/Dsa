import heapq

class Solution:
    def max_of_subarrays(self, l1, n, k):
        hq = []
        heapq.heapify(hq)
        res = []
        for i in range(n):
            if(i < k-1):
                heapq.heappush(hq, [-l1[i], i])
                continue
            heapq.heappush(hq, [-l1[i], i])
            while(True):
                root = hq[0]
                if(self.isRange(root[1], i, k-1)):
                    res.append(-root[0])
                    break
                heapq.heappop(hq)
        return res
    def isRange(self,root, i, k):
        if(root >= i-k):
            return 1
        return 0
