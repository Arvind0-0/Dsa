class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        lo = float('inf')
        for i in range(1, len(stalls)):
            lo = min(lo, stalls[i]-stalls[i-1])
        
        hi = stalls[-1]-stalls[0]+1

        def ok(d, k):
            p = float('-inf')
            for stall in stalls:
                if stall-p >= d:
                    k -= 1
                    p = stall
            return k <= 0
            
        while lo < hi:
            mi = lo+(hi-lo)//2
            if ok(mi, k):
                lo = mi+1
            else:
                hi = mi
        
        return lo-1
