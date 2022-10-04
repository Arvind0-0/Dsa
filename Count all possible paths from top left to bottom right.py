dp = [[1] * n for x in range(m)]

        for i in range(1,m):

            for j in range(1,n):  

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]%(10**9+7)
