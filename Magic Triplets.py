class Solution:
	def countTriplets(self, arr):
	    n, ans = len(nums), 0
	    for i in range(n):
	        left, right = 0, 0
	        for j in  range(i+1, n):
	            if nums[j] > nums[i]:
	                right +=1
	        for k in range(i):
	            if nums[k] < nums[i]:
	                left +=1
	        ans += left*right
	        
	    return ans
	            
