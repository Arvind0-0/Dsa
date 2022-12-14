class Solution:
    def findRange(self, a, size):
    	arr = [1 if i == '0' else -1 for i in a]
    	
    	l, r, res = 0, 0,[0, 0]
    	
    	cursum, maxsum = 0, float('-inf')
    	
    	for i in range(len(arr)):
    	    if arr[i] > arr[i] + cursum:
    	        l = i
    	        cursum = arr[i]
    	        
    	    else:
    	        cursum = arr[i] + cursum
    	        
    	    r = i
    	    if cursum > maxsum:
    	        maxsum = cursum
    	        res = [l + 1, r + 1]
    	        
    	return res if maxsum >= 0 else [-1]
