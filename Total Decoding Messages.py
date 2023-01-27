class Solution:
    def CountWays(self, str):
        n = len(str)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if str[0] != '0' else 0
        for i in range(2, n + 1):
            if str[i - 1] != '0':
                dp[i] += dp[i - 1]
            if str[i - 2] == '1' or (str[i - 2] == '2' and str[i - 1] <= '6'):
                dp[i] += dp[i - 2]
            dp[i] %= 10**9 + 7
        return dp[n]
