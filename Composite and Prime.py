class Solution:
	def Count(self, L, R):
		if L==1:
		    L+=1
		ans=0
		dp = [True]*(R+1)
		i=2
		while i*i <= R:
		    if dp[i]==True :
		        for j in range(i*i,R+1,i):
		            dp[j]=False
		    i+=1
		comp,prime = 0,0
		for i in range(L,R+1):
		    if(dp[i]):
		        prime+=1
		    else:
		        comp+=1
		return comp-prime
