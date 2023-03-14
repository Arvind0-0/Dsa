    def maxCoins(self, N, a):
        dp = [[0]*N for _ in range(N)]
        
        for left in range(N, -1, -1):
            for right in range(left, N):
                for k in range(left, right+1):
                    v = a[k]
                    if left-1 >= 0:
                        v *= a[left-1]
                    if right+1 < N:
                        v *= a[right+1]
                    if left <= k-1:
                        v += dp[left][k-1]
                    if k+1 <= right:
                        v += dp[k+1][right]
                    dp[left][right] = max(dp[left][right], v)
        
        return dp[0][N-1]
