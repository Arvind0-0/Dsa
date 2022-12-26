class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_range = nums[0]
        for i in range(0, len(nums)-1):
            cur_range = max(cur_range - 1, nums[i])
            if cur_range == 0:
                return False
        return True
