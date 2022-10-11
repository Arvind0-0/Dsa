class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = sys.maxsize
        smallest = INF 
        middle = INF
        for cur_num in nums:
            if cur_num <= smallest: 
                smallest = cur_num
                
            elif cur_num <= middle: 
                middle = cur_num
            else: 
                return True
        return False