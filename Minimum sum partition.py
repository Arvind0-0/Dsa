class Solution:
	def minDifference(self, arr, N):
        Sum = sum(arr)
        dp = {}
        def solve(n,p1,Sum):
            p2 = Sum - p1
            if n == 0:
                return p1-p2
            elif (n,p1) in dp:
                return dp[(n,p1)]
            else:
                item = arr[n-1]
                if p1-item >= p2+item:
                    c1 = solve(n-1,p1-item,Sum)
                    c2 = solve(n-1,p1,Sum)
                    c = min(c1,c2)
                else:
                    c = solve(n-1,p1,Sum)
                dp[(n,p1)] = c
                return c
        return solve(N,Sum,Sum)
        
