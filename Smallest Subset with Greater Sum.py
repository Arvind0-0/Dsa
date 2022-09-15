def minSubset(self, A,N):
        A.sort()
        c = 0
        Ts  = sum(A)
        cs = 0
        for i in range(N-1,-1,-1):
            cs+=A[i]
            Ts-=A[i]
            c+=1
            if Ts<cs:
                return c
            
        return c
