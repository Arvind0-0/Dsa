class Solution:
    def totalWays(self, n, c):
        m=1000000007
        p=1
        c.sort()
        p=1
        if n==1:
            return c[0]
        for i in range(n):
            p=(p*(c[i]-i))%m
        return p
