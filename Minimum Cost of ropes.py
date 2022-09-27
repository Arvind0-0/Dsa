from heapq import heapify,heappush,heappop
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        heapify(arr)
        res = 0
        
        while len(arr) > 1:
            first,second = heappop(arr),heappop(arr)
            
            res += first + second
            
            heappush(arr,first + second)
            
        return res
