from math import sqrt
class Solution:
    def check(self, n):
        flag = 1
        if n>1:
            for i in range(2, int(sqrt(n))+1):
                if n%i==0:
                    flag = 0
                    break
            if flag==0:
                return 0
            else:
                return 1
        return 0
        
    def isSumOfTwo (self, N):
        if N%2==0:
            return 'Yes'
        else:
            a = N-2
            if self.check(a):
                return 'Yes'
            return 'No'
