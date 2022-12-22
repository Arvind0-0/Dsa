class Solution:

    def findSubArrays(self,arr,n):
        if n == 1:
            if arr[0] == 0:
                return 1
            else:
                return 0
        su = 0
        dic = {}
        dic[0] = 1
        count = 0
        for ele in arr:
            su += ele
            if su in dic:
                if dic[su] > 1:
                    count += dic[su]
                else:
                    count += 1
                dic[su] += 1
            else:
                dic[su] = 1
        return count
