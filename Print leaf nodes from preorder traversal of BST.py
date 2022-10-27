class Solution:
	def leafNodes(self, arr, N):
		
		ret = []
		def collect(xs):
		    nonlocal ret
		    if len(xs) <= 1:
		        if xs:
		            ret.append(xs[0])
		        return
		    
		    collect([x for x in xs if x < xs[0]])
		    collect([x for x in xs if x > xs[0]])
		    
	    collect(arr)
	    return ret
