class StockSpanner:

    def __init__(self):
        self.stk = deque()

    def next(self, price: int) -> int:
        ans = 1
        while self.stk and self.stk[-1][0] <= price:
            ans+=self.stk.pop()[1]
        self.stk.append([price,ans])
        return ans
