def countPaths (self, N):
        if N==1: return 0
        MOD = 10**9+7
        p2, p1 = 0, 1
        for i in range(2,N):
            p2, p1 = p1, (2*p1 + 3*p2)%MOD
        ans = (3*p1)%MOD
        return ans
