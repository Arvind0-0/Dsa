from collections import defaultdict, Counter
from math import factorial
class Solution: 
    def luckyPermutations(self, N, M, A, graph):
        def _lobit(n): return n & (-n)
        A = [v-1 for v in A]
        adjs = defaultdict(list)
        prev, cur = {}, {}
        vimap = [0]* N
        for i,v in enumerate(A):
            vimap[v] |= (1<<i)
        for a,b in graph: 
            if a==b: continue
            a,b = a-1,b-1
            adjs[a].append(b)
            adjs[b].append(a)
        for v in range(N):
            if not vimap[v]: continue
            sig = _lobit(vimap[v])
            prev[ (sig, v) ] = 1            
            
        for _ in range(2, N+1): # chain length
            for (sig, ev), cnt in prev.items():
                for cand in adjs[ev]:
                    bits = vimap[cand]
                    availbits = bits & ~sig
                    if availbits:
                        newsig = sig | _lobit(availbits)
                        cur[(newsig, cand)] = cnt + cur.get((newsig, cand), 0)
            prev, cur = cur, prev
            cur.clear()
        
        fac_mul = 1
        for v in Counter(A).values(): fac_mul *= factorial(v)
        ans = sum(prev.values()) * fac_mul
        return ans
