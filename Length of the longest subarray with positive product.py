from math import inf
class Solution:
    def maxLength(self,arr,n):
        res = 0
        neg_len, pos_len = -inf, -inf
        for a in arr:
            if a == 0:
                neg_len, pos_len = -inf, -inf
            elif a > 0:
                neg_len, pos_len = neg_len + 1, max(1, pos_len + 1)
            else:
                neg_len, pos_len = max(1, pos_len + 1), neg_len + 1
            res = max(res, pos_len)
        return res
