class Solution:
    def maxSumLCM (self, n):
        count = 0
        for i in range(1, int(n**(1/2))+1):
            if n%i==0:
                count+=i
                if i!=n//i:
                    count+=(n//i)
        return count
