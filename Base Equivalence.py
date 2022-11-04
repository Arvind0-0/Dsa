from math import log,ceil
class Solution:
	def baseEquiv(self, n, m):
		# code here
		for r in range(2,33):
		    if ceil(log(n,r))==m:
		        return 'Yes'
		return 'No'
