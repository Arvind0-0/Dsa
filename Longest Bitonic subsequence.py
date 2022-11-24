from bisect import bisect_left
from math import inf

class Solution:
    def getLIS(self, nums):
        n = len(nums)
        lis = [1]*n
        d = [inf]*(n+1)
        d[0] = -inf
        for i in range(n):
            j = bisect_left(d, nums[i])
            lis[i] = j
            d[j] = nums[i]
        return lis
        
	def LongestBitonicSequence(self, nums):
        return max(l+d-1 for l, d in zip(self.getLIS(nums), self.getLIS(nums[::-1])[::-1]))
