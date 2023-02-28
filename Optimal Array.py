from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:

        currAns = 0

        res = []

        for i in range(n):

            currAns += (a[i] - a[i//2])

            res.append(currAns)

        return res
