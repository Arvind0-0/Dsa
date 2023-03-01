    def updateQuery(self, N, Q, U):
        BCNT = 17
        upd = [[] for _ in range(N+1)]
        tmp, bits = 0, [0]*BCNT
        for l, r, x in U:
            upd[l-1].append(x)
            upd[r].append(-x)
            
        ans = [0] * N
        for i in range(N):
            if upd[i]:
                for v in upd[i]:
                    v, sign = (v, 1) if v>0 else (-v, -1)
                    for j in range(BCNT):
                        if v & (1<<j): bits[j] += sign
                tmp = 0
                for j in range(BCNT):
                    if bits[j]: tmp |= (1<<j)
            ans[i] = tmp
        return ans
