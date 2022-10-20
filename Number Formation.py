from itertools import product
MOD = 10**9+7
class Solution:
	def getSum(self, X, Y, Z):
	    ans = 0
		dp = { (0,0,0):(1,0) } # { (x,y,z): (count, sum) }
		for x,y,z in product(range(X+1), range(Y+1), range(Z+1)):
		    if (x,y,z) in dp: continue
            mul = (10**(x+y+z-1)) % MOD
            _subcnt, _subsums = [0]*3, [0]*3
            if x>0: _subcnt[0], _subsums[0] = dp[(x-1, y, z)]
            if y>0: _subcnt[1], _subsums[1] = dp[(x, y-1, z)]
            if z>0: _subcnt[2], _subsums[2] = dp[(x, y, z-1)]
            cnt = sum(_subcnt)
            sums = (sum(_subsums) + mul*(_subcnt[0]*4 + _subcnt[1]*5 + _subcnt[2]*6)) % MOD
            dp[(x,y,z)] = (cnt, sums)
            ans = (ans + sums)%MOD
		return ans
