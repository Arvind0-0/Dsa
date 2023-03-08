class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1,max(piles)), True , key=lambda t:sum(ceil(pile/t) for pile in piles)<=h )+1
        # Tips: time list start at 1 because can't divide by zero
