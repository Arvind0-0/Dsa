
import math 

class Solution:    
    def maxGcd(self,N):
        #code here
        ans1=N*(N-1)
        ans2=(N-1)*(N-2)
        i1=N-2
        

        count=0
        while i1>=0:
            if math.gcd(ans1, i1)==1:
                ans1*=i1
                count+=1
            if count==2:
                break
            i1-=1
        i2=N-3
        count=0
        while i2>=0:
            if math.gcd(ans2, i2)==1:
                ans2*=i2
                count+=1
            if count==2:
                break
            i2-=1
        return max(ans1, ans2)
