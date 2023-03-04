def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        def _solve(ix):            
            if cs[ix]:
                for c in cs[ix]: _solve(c)
                dp[ix] = max( A[ix] - A[i] + cmax[i] for i in cs[ix] )
                cmax[ix] = max( dp[i] for i in cs[ix] )
            else:
                dp[ix] = A[ix]
                cmax[ix] = 0

        cs = [[] for _ in range(N)]
        dp, cmax = [0] * N, [0] * N
        for i in range(1, N): cs[P[i]-1].append(i)
        _solve(0)
        return max(dp)
