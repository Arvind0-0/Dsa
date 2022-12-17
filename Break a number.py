class Solution:
    
    def waysToBreakNumber(self, n):
        #code here
        m = 1000000000+7
        ans = (((n+1)*(n+2)%m)/2)%m
        return int(ans)
