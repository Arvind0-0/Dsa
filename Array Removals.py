from bisect import *
class Solution:
	def removals(self, a, n, t):
	    a = sorted(a)
        return min([n-((k)-(bisect(a, a[k]-t))+1) for k in range(n-1, -1, -1)])
