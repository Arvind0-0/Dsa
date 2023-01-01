import math

 

class Solution:

    def nCr(self, n, r):

        f = math.factorial

        return f(n) // f(r) // f(n-r)

        

    def compute_value(self, n):

 

        return self.nCr(2*n, n)%1000000007
