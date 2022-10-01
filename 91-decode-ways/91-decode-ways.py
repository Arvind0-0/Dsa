class Solution:
    def numDecodings(self, s: str) -> int:
        n= len(s)
        d = dict()
        def fun(i):
            if i==n:
                return 1
            if i in d:
                return d[i]
            count = 0            
            if s[i]=="0":
                count = 0
            elif i<n-1 and int(s[i:i+2])<=26:
                count = fun(i+1) + fun(i+2) 
            else:
                count = fun(i+1)
                
            d[i] = count
            return count
        
        return fun(0)