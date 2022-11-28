class Solution:
	def findSubarray(self,a, n):
        # code here
            start=0
            stop=-1
            i,j,mx,sm=0,0,0,0
            while j<n:
                if a[j]>=0:
                    sm+=a[j]
                    j+=1
                else:
                    if mx<sm:
                        mx=sm
                        start=i
                        stop=j-1
                    sm=0
                    j+=1
                    i=j
            if mx<sm:
                mx=sm
                start=i
                stop=j-1
            res=[]
            # print(start, stop)
            for i in range(start, stop+1):
                res.append(a[i])
            if len(res)==0:
                res.append(-1)
            return res
