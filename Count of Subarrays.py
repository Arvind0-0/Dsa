class Solution:
	def countSubarray(self,arr, n, k):
	    ans = 0
	    num = 0
	    for i in range(n):
	        if arr[i] > k:
	            num = i +1
            ans += num
        return ans
