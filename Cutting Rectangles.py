import math
class Solution:
    def minimumSquares(self, L, B):
        # code here
        gcd = math.gcd(L, B)
        return [(L // gcd) * (B // gcd), gcd]
