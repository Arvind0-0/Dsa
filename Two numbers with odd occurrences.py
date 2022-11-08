from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        d=Counter(Arr)
        res=[]
        for i, j in d.items():
            if j%2!=0:
                res.append(i)
        res=sorted(res)
        x=res[::-1]
        return x
