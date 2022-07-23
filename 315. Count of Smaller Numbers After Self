from sortedcontainers import SortedList

class Solution(object):
    def countSmaller(self, nums):
        res = []
        sorted_nums = SortedList(nums)
        for e in nums:
            idx = sorted_nums.index(e)
            res.append(idx)
            sorted_nums.remove(e)
        return res
