from collections import Counter
class Solution:
    def minFind(self, n, a):
        # code here
        dic=Counter(a)

        if (dic['R']%2==0 and dic['G']%2==0 and dic['B']%2==0) or (dic['R']%2!=0 and dic['G']%2!=0 and dic['B']%2!=0):
            return 2
        else:
            return 1
