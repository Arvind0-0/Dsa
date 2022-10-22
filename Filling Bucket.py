def fillingBucket(self, N):

        m=10**8

        dp=[0]*(N+1)

        dp[0]=dp[1]=1

        for i in range(2,N+1):

            dp[i]=(dp[i-1]%m + dp[i-2]%m)%m

 

        return dp[N]%m
