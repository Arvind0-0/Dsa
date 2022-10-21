class Solution:
	def reverseSpiral(self, R, C, a):
		# code here
		res = []
		t = R*C
		i,j = 0,0
		r,c = R-1,C-1
		cnt = 0
		while(cnt<t):
		    if(cnt<t):
		        for k in range(j,c+1):
		            res.append(a[i][k])
		            cnt+=1
	            i+=1
	        if(cnt<t):
	            for k in range(i,r+1):
	                res.append(a[k][c])
	                cnt+=1
	            c-=1
	        if(cnt<t):
	            for k in range(c,j-1,-1):
	                res.append(a[r][k])
	                cnt+=1
                r-=1
            if(cnt<t):
                for k in range(r,i-1,-1):
                    res.append(a[k][j])
                    cnt+=1
                j+=1
        return res[::-1]
