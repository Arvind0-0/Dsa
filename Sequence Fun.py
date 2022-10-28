class Solution:
	def NthTerm(self, n):
        mod=1000000007
        ans=1
		for i in range(1,n+1):
		    ans=(ans*i+1)%mod
        return ans;
