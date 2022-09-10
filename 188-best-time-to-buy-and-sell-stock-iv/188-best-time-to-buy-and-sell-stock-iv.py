class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        _p = [1000] + prices + [0]
        _vp = (y for x, y, z in zip(_p, _p[1:], _p[2:]) if (x < y) ^ (y < z))
        
        profits, vp = [], []
        for v, p in zip(_vp, _vp):
            while vp and (v < vp[-1][0] or p >= vp[-1][1]):
                pv, pp = vp.pop()
                if pv < v:
                    v, pv = pv, v
                profits.append(pp - pv)
            vp.append((v, p))
        else:
            profits.extend(p - v for v, p in vp)

        return sum(nlargest(k, profits))