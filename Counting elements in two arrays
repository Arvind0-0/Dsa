from bisect import bisect_right
class Solution:
    def countEleLessThanOrEqual(self,arr1,m,arr2,n):
        #returns the required output
        arr2.sort()
        res = []
        
        for num in arr1:
            res.append(bisect_right(arr2,num))
        return res
